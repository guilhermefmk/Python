'''
Listas em Python
fatiamento
append, insert, pop, del ,clear, extend, +
min, max
range
'''

# lista = [1, 2, 3, 4, 5, 6]
# print(lista[0:3])
# print(lista[::-1])
# print(lista[:3])
# print(lista[::2])

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2            #################   SOMA DUAS LISTAS ITERANDO AO FINAL DA PRIMEIRA
l1.extend(l2)           #################   SOMA DUAS LISTAS ITERANDO AO FINAL DA PRIMEIRA
l1.extend('a')          #################   INSERE UM NOVO VALOR AO FINAL DA LISTA
l2.append('b')          #################   INSERE UM NOVO VALOR AO FINAL DA LISTA
l2.insert(0 , 'banana') #################   INSERE UM NOVO VALOR NO INDICE INDICADO MOVENDO O RESTANTE DOS VALORES PARA OS INDICES A FRENTE
l2.pop()                #################   REMOVE O ÙLTIMO ELEMENTO DA LISTA
del(l2[3:5])            #################   DELETA ELEMENTOS DA LISTA
print(l1)
print(l2)
print(l3)
print(max(l3))          #################   MAIOR ELEMENTO DA LISTA
print(min(l3))          #################   MENOR ELEMENTO DA LISTA


l4 = list(range(1,9,3))   #################   CRIA UMA LISTA NO RANGE DEFINIDO
print(l4)

for valor in