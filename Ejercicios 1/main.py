from lexer_class import LexerClass

l = LexerClass()
l.test('2 * 3 =')

from lexer_function import LexerFunction, test

l = LexerFunction()
test(l, "1 / 2 =")
    