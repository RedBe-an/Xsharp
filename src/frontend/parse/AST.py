
class Program:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program({self.statements})"

class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name} = {self.value}"

class Print:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f"print({self.message})"

class IfStatement:
    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return f"if {self.condition} then {self.then_branch} else {self.else_branch}"

class Comparison:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"{self.left} {self.operator} {self.right}"