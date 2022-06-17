'''
Faça um programa que peça ao user para digitar um número inteiro,
informe se este número é pai ou ìmpar. Caso o user não digite um número  inteiro,
informe que não é um número inteiro
'''
numero = input('Digite um número: ')

if numero.isdecimal():
    numero = int(numero)
    if numero % 2 == 0:
        print('É par')
    else:
        print('É impar')
else:
    print('Não é um número inteiro')