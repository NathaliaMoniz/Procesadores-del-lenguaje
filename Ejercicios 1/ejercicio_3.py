import ply.lex as lex

tokens = (
    "ONE_LINE_COMMENT",
    "MULTI_LINE_COMMENT",
    "NAME",
    "ASSIGN",
    "NUMBER"
)

# 1) comentario de una línea

t_ONE_LINE_COMMENT = r'\#.*'

# 2) comentario multilinea completo

t_MULTI_LINE_COMMENT = r'\/\*(.|\n)*?\*/'

t_NAME = r'[a-zA-Z][a-zA-Z0-9_]*'

def t_newline(token):
    r'\n+'
    # aumenta la posicion de la linea tantos \n
    token.lexer.lineno = token.value.count('\n')

def t_error(token):
    # imprime información sobre el error
    print("[Ex1][Lexer] Illegal character", token.value)
    # se salt la linea del error
    token.lexer.skip(1)

lexer = lex.lex()

# input para el lexer
lexer.input("/* jajaja \n jajaja*/")
for token in lexer:
    print(token.type, token.value)

