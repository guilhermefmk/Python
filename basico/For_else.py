lista = ['Guilherme', 'JCunha', 'Complexo', 'Joao']

for valor in lista:
    if valor.lower().startswith('j'):
        print(valor)
        break
else:
    print('Não existe palavra com J')