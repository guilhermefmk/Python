'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''

nome = input("Digite seu primeiro nome: ")

if len(nome)<4:
    print(f'{nome} é curto')
elif len(nome)>6:
    print(f'{nome} é muito grande')
else:
    print(f'{nome} é normal')