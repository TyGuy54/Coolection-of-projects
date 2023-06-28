from tokens import Token, TokenType


WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.advance

    # moves to the next character, if theres none it stops
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None