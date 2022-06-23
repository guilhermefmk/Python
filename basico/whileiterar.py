frase = 'o rato roeu a roupa do rei de roma'
tam = len(frase)
contador = 0
nova_string = ''

while contador < len(frase):
    # if frase[contador] != " ":
    # print(frase[contador])
    if frase[contador - 1] == ' ' and frase[contador + 1] != ' ':
        nova_string += frase[contador].upper()
    else:
        nova_string += frase[contador]
    contador += 1
print(nova_string)