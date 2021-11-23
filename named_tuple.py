"""
Modulo Collection - Name tuple

tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tupla, diferenciadas onde especificamos um nome para a mesma
e também parametro

"""
# Import

from collections import namedtuple

# Forma 1

cachorro = namedtuple('cachorro', 'idade raça nome')


# Forma 2

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# usando

ray = cachorro(idade=2, raça='Chow Chow', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1

print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2

print(ray.idade)
print(ray.raça)
print(ray.nome)

print(ray.index('Chow Chow'))

print(ray.count('Chow Chow'))