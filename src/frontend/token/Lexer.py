import re
import logging

from frontend.token.Token import Token
from shared.TokenType import TokenType

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

class Lexer:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        logging.debug("Initialized lexer with source: %s", source)

    def tokenize(self):
        logging.debug("Starting tokenization")
        token_specification = [
            (TokenType.BEGIN, r'Once upon a time'),
            (TokenType.COMMA, r','),
            (TokenType.IDENTIFIER, r'[a-zA-Z_]\w*'),
            (TokenType.PERIOD, r'\.'),
            (TokenType.ASSIGN, r'was'),
            (TokenType.NUMBER, r'\d+'),
            (TokenType.IF, r'If'),
            (TokenType.LESS_THAN, r'was less than'),
            (TokenType.THEN, r'then'),
            (TokenType.PRINT, r'And'),
            (TokenType.STRING, r'"[^"]*"'),
            (TokenType.ELSE, r'Otherwise,'),
            (TokenType.END, r'The end\.'),
            (None, r'\s+'),  # Skip whitespace
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        get_token = re.compile(tok_regex).match
        pos = 0
        while pos < len(self.source):
            match = get_token(self.source, pos)
            if not match:
                logging.error("Unexpected character: %s", self.source[pos])
                raise RuntimeError(f'Unexpected character: {self.source[pos]}')
            type = match.lastgroup
            if type:
                value = match.group(type)
                if type != None:
                    token = Token(type, value)
                    self.tokens.append(token)
                    logging.debug("Created token: %s", token)
            pos = match.end()
        logging.debug("Finished tokenization with tokens: %s", self.tokens)
        return self.tokens