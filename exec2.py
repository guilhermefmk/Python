'''
Faça um programa que pergunte  a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
'''


hora, min = [int(x) for x in input('Qual a hora atual? ex. HH-MM\n').split('-')]



if 0<=hora<12:
    print("Bom dia!")
elif 12<=hora<18:
    print("Boa tarde!")
else:
    print("Boa noite!")