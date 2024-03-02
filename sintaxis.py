import ply.lex as lex
import ply.yacc as yacc
import sys

literals = ('=', ';') # tinene que ser caracteres de longitud 1

tokens = ('ID', 'NUMBER')

t_ID = r'[a-zA-Z][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("[Lex Error] At value", t.value)

lexer = lex.lex()
file = open(sys.argv[1])
content = file.read()
lexer.input(content)

for token in lexer:
    print(token.type, token.value, token.lineno)