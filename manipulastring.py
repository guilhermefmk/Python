'''
Manipulando Strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
'''
# positivos   [012345678]
texto       = 'Python s2'
# negativos  -[987654321]
# INDICES
for i in texto:
    print(i)
# POSITIVOS
for i in range(len(texto)):
    print(f'texto[{i}] =', texto[i])
# NEGATIVOS
for i in range(-(len(texto)),0,1):
    print(f'texto[{i}] =', texto[i])

# texto[1] = 'i' ############### ERRO

nova_string = texto[2:6] # Fatiando Strings - (STRING)[(INDICE INICIAL):(INDICE FINAL + 1): (PASSO)]
nova_string1 = texto[:6]
nova_string2 = texto[3:]
nova_string3 = texto[-9:-3]
nova_string4= texto[:-1]
nova_string5= texto[::-1] # inverter string

print(nova_string)
print(nova_string1)
print(nova_string2)
print(nova_string3)
print(nova_string4)
print(nova_string5)


