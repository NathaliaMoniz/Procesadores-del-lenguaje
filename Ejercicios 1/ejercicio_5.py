import ply.lex as lex

tokens = (
    "INTEGER",
    "FLOAT"
)
def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t

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
lexer.input("2.1")
for token in lexer:
    print(token.type, token.value)