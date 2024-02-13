import ply.lex as lex

reserved = (
    'VAR', 'WHILE'
)

tokens = (
    'LBRACKET',
    'RBRACKET',
    'ID',
    'NUMBER',
    'LT',
    'LE',
    'GT',
    'GE',
    'EQ',
    'NE'
) + reserved

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r

t_ignore = ' \t\x0c'

t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'=>'
t_EQ = r'=='
t_NE = r'!='
def t_NUMBER(t):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    return t 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_map.get(t.value,'ID')    # Check for reserved words
    return t

def t_error(token):
    # imprime información sobre el error
    print("[Ex1][Lexer] Illegal character", token.value)
    # se salt la linea del error
    token.lexer.skip(1)