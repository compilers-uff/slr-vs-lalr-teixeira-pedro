# Programa principal slrvslalr : aqui é implementada a parte da análise sintática da gramática
#juntamente com a main, onde se opta por usar ou LALR ou SLR

import ply.yacc as YACC
from termcolor import colored
from exprelex import tokens


print('[TOKENS]',tokens)

# trata a regra S → L = R
# adicionada regra semântica pra guardar no valor a seguinte regra : S.value = L.value + " ← " + R.value
def p_eS_atrib(p):
    'S : L ATRIBUICAO R'
    p[0] = p[1] + '←' + p[3]

# trata a regra S → R
# adicionada regra semântica pra guardar no valor a seguinte regra : S.value =  R.value
def p_eS_eR(p):
    'S : R'
    p[0] = p[1]

# trata a regra L → * R
# adicionada regra semântica pra guardar no valor a seguinte regra : L.value  = " [*ptr] " + R.value
def p_eL_pointer_eR(p):
    'L : PONTEIRO R'
    p[0] = '[*ptr] ' + p[2]

# trata a regra L → id
# adicionada regra semântica pra guardar no valor a seguinte regra : L.value = get_lexval(id)
def p_eL_ide(p):
    'L : ID'
    p[0] = p[1]

# trata a regra R → L
# adicionada regra semântica pra guardar no valor a seguinte regra : R.value =  L.value
def p_eR_eL(p):
    'R : L'
    p[0] = p[1]

parser=None
#trata os erros de sintaxe caso seja inserido
def p_error(p):
    print(colored("ERRO DE SYNTAX!!!",color='red'))
    exit(1)

#input , opção 1 SLR , 2 LALR
resp=input("TECLE [1] PARA USAR SLR, E [2] PARA LALR :/$> ")

# montando o parser
if int(resp) not in [1,2] :
    print(colored('[OPÇÃO ERRADA]',color='red'))
    exit(1)
elif int(resp)==1:#SLR
    parser = YACC.yacc(method='SLR',debug=1,write_tables=1,debugfile='slr_.out',tabmodule="SLR_tabela")
    print(colored('[USANDO SLR]',color='yellow'))
elif int(resp)==2:#LALR
    parser = YACC.yacc(method='LALR',debug=1,write_tables=1,debugfile='lalr_.out',tabmodule="LALR_tabela")
    print(colored('[USANDO LALR]',color='green'))

#loop infinito para inserção de strings para parsear (inserção que seja fora da gramática para o loop)
while True:
    try:
        s= input(">>>")
    except EOFError:
        break
    if not s: continue
    #faz o parse
    result= parser.parse(s,tracking=True)
    # mostra a saída do  que foi guardado em S.value após o parsing da entrada (print(S.value))
    print(result)

