'''
CPF = 168.995.350-09
---------------------------------------------------------------
1 * 10 = 10                     #    1 * 11 = 11 <-
6 * 9  = 54                     #    6 * 10 = 60
8 * 8  = 64                     #    8 * 9 = 72
9 * 7  = 63                     #    9 * 8 = 72
9 * 6  = 54                     #    9 * 7 = 63
5 * 5  = 25                     #    5 * 6 = 30
3 * 4  = 12                     #    3 * 5 = 15
5 * 3  = 15                     #    5 * 4 = 20
0 * 2  = 0                      #    0 * 3 = 0
                                # -> 0 * 2 = 0
         297                    #            343
11 - (297 % 11) = 11            #    11 - (343 % 11) = 9
11 > 9 = 0                      #
Digito 1 = 0                    #    Digito 2 = 9
'''
while True:
    cpf =  input("Digite seu cpf: (Para finalizar digite 'EXIT')\n")
    lista = []
    soma1 = 0
    soma2 = 0
    if cpf == 'EXIT':
        break
    for x in cpf:
        if x.isdigit():
            x = int(x)
            lista.append(x)
    ultimo = lista.pop()
    for n , x in enumerate(range(11,1,-1)):
        if x == 11:
            soma2 += lista[n] * x
        else:
            soma2 += lista[n] * x
            soma1 += lista[n-1] * x
    lista.append(ultimo)
    primeiro_dig = 11 - (soma1 % 11)
    segundo_dig = 11 - (soma2 % 11)

    if primeiro_dig > 9:
        primeiro_dig = 0
    if segundo_dig > 9:
        segundo_dig = 0
    if primeiro_dig == lista[len(lista) - 2] and segundo_dig == lista[len(lista) - 1]:
        print("CPF EH VALIDO!!")
    else:
        print("CPF EH INVALIDO!!")

