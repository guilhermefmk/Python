'''
1 - Crie uma função que recebe o valor da função 2 como parâmetro e retorne o valor da função 2 executada
'''


def func1(funcao, *args, **kwargs):
    return print(funcao(*args, **kwargs))



def fala_oi(nome):
    return f'Oi {nome}'


def saudacao1(nome, saudacao):
    return f'{saudacao} {nome}'


func1(fala_oi, 'Guilherme')
func1(saudacao1, 'Guilherme', 'Bom dia')
