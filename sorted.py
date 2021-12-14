"""

Sorted

OBS: Não confunda com a função sort(). O sort() só funciona em listas

Podemos utilizar o sorted() com qualquer iteravel

como o proprio nome diz, sorted() serve para ordenar

OBS: O sorted, SEMPRE retorna uma Lista com os elementos do iteravel ordenados

# Exemplo

numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))  # Ordenar do menos para o maior

print(numeros)

numeros = [6, 1, 8, 2]
print(numeros)

print(tuple(sorted(numeros)))
# Adicionando parametros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username. Ordem Alfabética

print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))


"""

# Ultimo exemplo

musica = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Lambada", "tocou": 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musica, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musica, key=lambda musica: musica['tocou'], reverse=True))