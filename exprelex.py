#implementa a parte léxica

import ply.lex as LEX
#import re

# OS TOKENS
tokens=(
    'ATRIBUICAO',
    'PONTEIRO',
    'ID'
)

# REGEXP PROS TOKENS
t_ATRIBUICAO = r'\='
t_PONTEIRO = r'\*'

# REGEXP do identificador (ID)
def t_ID(t):
    r'[a-zA-Z][\w]*'
    t.value=str(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore=' \t'

def t_error(t):
    print("caractere ilegal %s " % t.value[0])
    t.lexer.skip(1)


lexer = LEX.lex()
