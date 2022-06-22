secreto = 'perfume'
lista = []
listaoculta = []
digitadas = []
contador = 5
for letra in secreto:
    lista.append(letra)
    listaoculta.append("_")

while True:
    print(listaoculta)
    letra = input(f"Chute uma letra: (Você tem {contador} chances)\n ")
    if len(letra) > 1 or letra.isdigit():
        print('Apenas uma letra')
        continue
    if letra not in secreto:
        digitadas.append(letra)
        contador -= 1
    if contador == 0:
        print(f'Você perdeu a palavra secreta era {secreto.upper()}')
    for n, j in enumerate(lista):
        if letra == j:
            listaoculta[n] = lista[n]
    print(f'As letras digitadas foram: {digitadas}')
    if "_" not in listaoculta:
        print(listaoculta)
        print("Você venceu!")
        break
