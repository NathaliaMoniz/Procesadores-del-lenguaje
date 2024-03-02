from lexer_class import LexerClass
import sys 
import ply.yacc as yacc
l = LexerClass()
l.test_with_files(sys.argv[1])

class parserClass:
    tokens = LexerClass.tokens

    def __init__(self):
        self.parser = yacc.yacc(module = self) # en lugar de self puedo poner un ficherodonde estan los tokens
        self.lexer = LexerClass().lexer
    
    def p_program(self, p):
        ''' program : line
                    | line NEW_LINE program'''
    def p_line(self, p):
        '''line : plus
                | minus'''
        print(p[1])
    
    def p_error(self, p):
        if p: print()
        else: print('Error EOF', p.value, p.lineno)

    def p_plus(self, p):
        ''' plus : NUMBER "+" NUMBER'''
        # print(p[1], p[2], p[3])
        p[0] = p[1] + p[3]
    
    def p_minus(self, p):
        ''' minus : NUMBER "-" NUMBER'''
        # print(p[1], p[2], p[3])
        p[0] = p[1] - p[3]

    def test(self, data):
        self.parser.parse(data)
    
    def test_with_files(self, path):
        file = open(path)
        content = file.read()  
        self.test(content)
