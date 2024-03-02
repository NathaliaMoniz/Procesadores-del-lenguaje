import ply.lex as lex
import sys

class LexerClass:
    tokens = ('NUMBER', 'NEW_LINE')
    literals = ('+', '-')

    def __init__(self):
        self.lexer = lex.lex(module = self)

    def t_NUMBER(self, t):
        r'[1-9][0-9]*'
        t.value = int(t.value)
        return t
    
    t_ignore =  ' \t'

    def t_error(self, t):
        print("[Lex Error] At value", t.value)

    def t_NEW_LINE(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count('\n')
        return t
    
    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token.type, token.value)
        
    
    def test_with_files(self, path):
        file = open(path)
        content = file.readlines()
        for line in content:
            self.test(line)
    

