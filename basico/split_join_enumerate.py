'''
Split, join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elemtos da lista # iteráveis
'''

# string = 'O Brasil é o país do futebol, o Brasil é penta.'
#
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
# print(lista_2)
# print(lista_1)
#


# lista = ['O', 'Brasil', 'é', 'penta']
# string = ' '.join(lista)
# print(string)

# string = 'O brasil é penta'
# lista = string.split(' ')
#
# for v1, v2 in enumerate(lista):
#     print(v1, v2)


# lista = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
# for n, v in enumerate(lista, 53):
#     print(v , n)
#
# lista1 = ['Luiz', 'João', 'Maria']
#
# n1, n2, n3 = lista1
#
# print(n2)

lista = ['Luiz', 'Joao', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8]

n1, n2, n3, *outra_lista, ultimo_lista = lista
print(n1, n2, outra_lista, ultimo_lista)