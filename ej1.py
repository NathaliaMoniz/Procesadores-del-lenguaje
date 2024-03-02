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


def p_program(p):
    '''program : assign ";"
               | assign ";" program''' 
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
    print(p[0])


def p_assign(p):
    '''assign : ID "=" NUMBER'''
    print(p[1]) # p1 representa el token ID
    p[0] = p[1] + p[2] +str(p[3])

def p_error(p):
    if p: print()
    else: print('Error EOF', p.value, p.lineno)

parser = yacc.yacc(debug = True)
file = open (sys.argv[1])
content = file.read()
parser.parse(content)
