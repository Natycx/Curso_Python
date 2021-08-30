"""
Tipo String

Em python, um dado é considerado do tipo string sempre que :
- Estiver entre aspas simples -> 'uma string' '235' 'a' 'True'
- Estiver entre aspas duplas -> "uma string" "235" "a" "True"
- Estiver entre aspas triplas -> '''uma string''' '''235''' '''a''' '''True'''


# True

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:4])  # Slice de string

print(nome[5:15])  # Slice de string

# [ 0,       1]
# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])


"""
# - Estiver entre aspas duplas triplas -> """uma string""" """235""" """a"""

# [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12,13, 14]
# ['G','e','e','k',' ','U','n','i','v','e','r','s','i',t,'y']
nome = 'Geek University'
"""
[::-1]-> Comece do primeiro elemento e vá até o ultimo elemento e inverta
"""
print(nome[::-1])   # Python

print(nome.replace('e', 'i'))

texto = 'socorram me subi no o nibus em marrocos'
print(texto)

print(texto[::-1])