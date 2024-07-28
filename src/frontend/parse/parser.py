import logging

from AST import Assignment, Comparison, IfStatement, Print, Program
from shared.TokenType import TokenType

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        logging.debug("Initialized parser with tokens: %s", tokens)

    def parse(self):
        logging.debug("Starting parse")
        self.consume(TokenType.BEGIN, "Expect 'Once upon a time' at the beginning of the program.")
        self.consume(TokenType.COMMA, "Expect ',' after 'Once upon a time'.")
        statements = []
        while not self.check(TokenType.END):
            statement = self.statement()
            if statement:
                statements.append(statement)
        self.consume(TokenType.END, "Expect 'The end.' at the end of the program.")
        logging.debug("Finished parse with statements: %s", statements)
        return Program(statements)

    def statement(self):
        logging.debug("Parsing statement at token: %s", self.peek())
        if self.check(TokenType.END):
            return None  # END는 별도로 처리되므로 여기서는 아무것도 반환하지 않음.
        elif self.check(TokenType.IDENTIFIER):
            if self.peek().value == "number":
                return self.declaration()
            else:
                return self.assignment()
        elif self.check(TokenType.PRINT):
            return self.print_statement()
        elif self.check(TokenType.IF):
            return self.if_statement()
        elif self.check(TokenType.ELSE):
            self.consume(TokenType.ELSE, "Expect 'Otherwise,' in if statement.")
            return None  # ELSE는 if_statement 내에서 처리되므로 여기서는 아무것도 반환하지 않음.
        else:
            self.error("Unexpected statement.")

    def declaration(self):
        logging.debug("Parsing declaration")
        self.consume(TokenType.IDENTIFIER, "Expect 'number' keyword.")
        name_token = self.consume(TokenType.IDENTIFIER, "Expect variable name.")
        self.consume(TokenType.PERIOD, "Expect '.' after variable declaration.")
        logging.debug("Finished parsing declaration: %s", name_token.value)
        return Assignment(name_token.value, None)

    def assignment(self):
        logging.debug("Parsing assignment")
        name_token = self.consume(TokenType.IDENTIFIER, "Expect variable name.")
        self.consume(TokenType.ASSIGN, "Expect 'was' after variable name.")
        value_token = self.consume(TokenType.NUMBER, "Expect a number.")
        self.consume(TokenType.PERIOD, "Expect '.' at the end of the assignment.")
        logging.debug("Finished parsing assignment: %s = %s", name_token.value, value_token.value)
        return Assignment(name_token.value, int(value_token.value))

    def print_statement(self):
        logging.debug("Parsing print statement")
        self.consume(TokenType.PRINT, "Expect 'And \"...\" was told to the world.'")
        message_token = self.consume(TokenType.STRING, "Expect a string.")
        self.consume(TokenType.PERIOD, "Expect '.' at the end of the print statement.")
        logging.debug("Finished parsing print statement: %s", message_token.value)
        return Print(message_token.value)

    def if_statement(self):
        logging.debug("Parsing if statement")
        self.consume(TokenType.IF, "Expect 'If'.")
        left = self.consume(TokenType.IDENTIFIER, "Expect variable name.")
        self.consume(TokenType.LESS_THAN, "Expect 'was less than'.")
        right = self.consume(TokenType.IDENTIFIER, "Expect variable name.")
        self.consume(TokenType.THEN, "Expect 'then'.")
        then_branch = self.statement()
        else_branch = None
        if self.match(TokenType.ELSE):
            else_branch = self.statement()
        logging.debug("Finished parsing if statement: if %s < %s then %s else %s", left.value, right.value, then_branch, else_branch)
        return IfStatement(Comparison(left.value, '<', right.value), then_branch, else_branch)

    def match(self, *token_types):
        for token_type in token_types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def consume(self, token_type, error_message):
        logging.debug("Consuming token: %s (expecting %s)", self.peek(), token_type)
        if self.check(token_type):
            return self.advance()
        self.error(error_message)

    def check(self, token_type):
        if self.is_at_end():
            return False
        return self.peek().type == token_type

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.peek().type == TokenType.END

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def error(self, message):
        logging.error("Error: %s", message)
        raise Exception(message)

