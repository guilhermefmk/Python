# a = lambda x, y: x * y
#
# print(a(2,3))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 4],
    ['P5', 45]
]

print(lista)
# def func(item):        ##  Puxa o indice 1 de cada posição de lista
#     return item[1]
# lista.sort(key=func)   ## Ordena de acordo com a key passada
lista.sort(key=lambda item: item[1])   # Mesma coisa de cima
print(lista)