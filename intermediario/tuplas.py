tupla1 = (1,2,3,4,5,6,7,'a')
tupla2 = 1,2,3,4,5,7,'a'
tupla3 = 1,
tupla4 = tupla1+tupla3
tupla5 = tupla3 * 5
print(tupla1)
print(tupla4)
print(tupla5)
tupla1 = list(tupla1)
print(tupla1, type(tupla1))
tupla1 = tuple(tupla1)
print(tupla1, type(tupla1))
