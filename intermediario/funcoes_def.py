'''
Funções em Python
'''

# def func(x):
#     print(x)
# def dumb():
#     return func
#
# x = dumb()('Panico na zona sul')


# def funcao(*args, **kwargs):
#     args = list(args)
#     argss = list(kwargs)
#     print(args)
#     print(argss)
# teste = [1,2,3]
# teste2 = ['a' , 'b', 'c']
# funcao(*teste, *teste2, nome='Guilherme')


variavel = 'valor'  #GLOBAL

def func():
    print(variavel)

def func2():
    global variavel # PUXANDO A VARIAVEL GLOBAL
    variavel = 'Outro valor' #PRIVADA
    print(variavel)
func()
func2()

print(variavel)