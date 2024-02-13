# 1) importar PLY Lex
import ply.lex as lex
import sys
# 2) definir tokens
tokens = (
    "PALABRA",
    "NUMERO"
)

t_PALABRA = r'[a-zA-Z][a-zA-Z0-9_]*'

# type, value, lineno (en que linea del fichero se ha encontrado), lexpos
def t_NUMERO(token):
    r'[1-9][0-9]*'
    token.value = int(token.value)
    return token

# va a ignorar el espacio vacío o la tabulación
t_ignore = ' \t'

def t_newline(token):
    r'\n+'
    # aumenta la posicion de la linea tantos \n
    token.lexer.lineno = token.value.count('\n')
def t_error(token):
    # imprime información sobre el error
    print("[Ex1][Lexer] Illegal character", token.value)
    # se salt la linea del error
    token.lexer.skip(1)

# 3) construir el lexer
lexer = lex.lex()

# input para el lexer
lexer.input("palabra variable_1 123 19")
for token in lexer:
    print(token.type, token.value)

"""file = open(sys.argv[1])
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)"""
