"""
Mapas = Conhecidos em Python como Dicionarios

# Iterar sobre dicionarios

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])


for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')


print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desenpacotamento de dicionarios
print(receita.items())

for chave, valor in receita.items():
    print(f'Chave = {chave} e valor = {valor}')


"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Soma, valor maximo*, valor minimo*, tamanho

# * Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
