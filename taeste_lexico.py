# usado para testar se a parte léxica está correta

from exprelex import lexer

data = '''
var1 = var2
x_1 = * x2
a  = *b
'''

lexer.input(data)

while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)