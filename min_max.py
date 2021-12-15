"""
Min e Max

max() - > Retorna o maior valor em um iteravel ou o maior de dois
ou mais elemento.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = 1, 8, 4, 99, 34, 129
print(max(tupla))

set = {1, 8, 4, 99, 34, 129}
print(max(set))

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dict))

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dict.values()))

# Faça um programa que receba dois valores do usuario e mostre o maior

vall = int(input('Informe o primeiro valor: '))
vall2 = int(input('Informe o segundo valor: '))

print(max(vall, vall2))

print(max(4, 67, 34))

print(max('a', 'abc', 'ab'))

print(max('a', 'b''c', 'g'))

print(max('Geek University'))

min() - Retorna o menor valor em um iteravel ou menor de dois ou mais elementos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = 1, 8, 4, 99, 34, 129
print(min(tupla))

set = {1, 8, 4, 99, 34, 129}
print(min(set))

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dict))

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dict.values()))

# Faça um programa que receba dois valores do usuario e mostre o maior

vall = int(input('Informe o primeiro valor: '))
vall2 = int(input('Informe o segundo valor: '))

print(min(vall, vall2))

print(min(4, 67, 34))

print(min('a', 'abc', 'ab'))

print(min('a', 'b''c', 'g'))

print(min('Geek University'))


# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nomes)))
print(min(nomes, key=lambda nome: len(nomes)))


"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Lambada", "tocou": 32},
]
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio! Imprima o titulo da musica
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])

max = 0

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])