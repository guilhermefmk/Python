'''
while em Python - Aula 7
utilizado para realizar ações enquanto
uma condição for verdadeira.

'''
x = 0
while x <= 100:
    if x % 2 == 1:
        x += 1
        continue # PULA PARA O PRÓXIMO LAÇO
        #break     FINALIZA O LAÇO
    else:
        print(x)
        x += 1
else:
    print('Cheguei no else')