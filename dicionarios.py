"""
Dicionario
Em outras linguagens conhecido como mapas

Dicionários são coleções do tipo chave/valor
Dicionários são representados por {}

print(type({}))

# Criação de dicionários

# Forma 1

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menso comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

"""


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Acessando elementos

# Forma 1 - acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
# print(paises['ru'])

# Obs: caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KayError

# Forma 2- Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))

