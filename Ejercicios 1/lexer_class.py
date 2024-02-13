import ply.lex as lex

class LexerClass:
    def __init__(self) -> None:
        self.lexer = lex.lex(module=self)
    
    tokens = (
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "EQUALS",
        "NUMBER"
    )

    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUALS = r'='
    
    def tNUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t
    
    t_ignore = ' \t'

    def t_NL(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count('\n')
        
