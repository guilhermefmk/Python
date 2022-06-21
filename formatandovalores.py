'''
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - inteiros (int)
:f - Números de ponto flutante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

'''
num = 1
string = 'EXEMPLO '
print(len('#########################'))
############################### SEÇÃO 1 ####################################################
print(f'\n\n{string + str(num):#^59}')

num_1 = 10
num_2 = 3
divisao = num_1/num_2
nome = 'Guilherme Cunha'

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
print(f'{nome:s}')


############################### SEÇÃO 2 ####################################################
print(f'\n\n{string + str(num+1):#^59}')

num_3 = 1
num_4 = 1150

print(f'{num_3:0>10}')
print(f'{num_4:0>10}')
print(f'{num_4:0>10.2f}')
print(f'{nome:*^37}')


############################### SEÇÃO 3 ####################################################
print(f'\n\n{string + str(num + 2):#^59}')

nome_formatado = '{:@>16}'.format(nome)
nome_formatado2 = '{n:0<20}{n}{n}{n}'.format(n=nome)  ######### SUCESS
# nome_formatado2 = '{}{}{}{}'.format(n=nome)  ########### ERROR

print(nome_formatado)
print(nome_formatado2)


############################### SEÇÃO 4 ####################################################
print(f'\n\n{string + str(num + 3):#^59}')

nome1 = 'Guilherme'
sobrenome1 = 'Cunha'
idade = 25
dados_formatados = 'Meu nome é {0}, meu sobrenome é {1} e eu tenho {2} anos de idade'.format(nome1, sobrenome1, idade)

print(dados_formatados)
