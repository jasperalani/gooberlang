from lexer import Lexer

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error_ = lexer.make_tokens()

    return tokens, error_
