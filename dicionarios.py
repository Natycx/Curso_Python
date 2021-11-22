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


# Acessando elementos

# Forma 1 - acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
# print(paises['ru'])

# Obs: caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KayError

# Forma 2- Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada n gerará erro
russia = paises.get('ru')

if russia:
    print('Encontrei o pais')
else:
    print('Não encontrei o pais')


# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o pais {pais}')


# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# podemos utilizar qualquer tipo de dado

# Tuplas por exemplos São bastante interessantes de serem utilizadas como chave de dicionario
# por serem imutaveis
localidades = {
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo'
}

print(localidades)
print(type(localidades))


# Adicionando elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'maio': 500}

receita.update(novo_dado)
print(receita)

# Atualizando dados

receita['maio'] = 550
print(receita)

# Forma 2

receita.update({'maio': 600})
print(receita)

# COnclusão 1 : A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
# Conclusão 2: em dicionarios, não podemos ter chaves repetidas
# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1
ret = receita.pop('mar')
print(ret)

print(receita)

# OBS: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um
# KeyError é retornado.
# OBS: Ao remover um objeto o valor deste objeto é sempre retornado

# Forma 2

del receita['fev']

print(receita)

# Se a chave n existir sera gerado um KeyError


"""

# Imagine um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos
"""
Carrinho de compras
    Produto 1
        - nome:
        - quantidade:
        -preço
    Produto 2
        - nome:
        - quantidade:
        - preço

# 1 - Podemos utilizar uma Lista

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teriamos que saber qual é o indice de cada informação de cada produto

# Forma 2 - Poderiamos utilizar uma tupla

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)

print(carrinho)

# Forma 3 - Poderiamos utilizar dicionario

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informações

# Metodos de dicionarios:

d = dict(a=1, b=2, c=3)

print(d)


# Limpar o dicionario
d.clear()
print(d)

# Copiando um dicionario para outro

# Forma 1
novo = d.copy()
print(novo)

novo['d'] = 4

print(d)
print(novo)


# Forma 2 # shallow copy

novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

"""

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nomes', 'pontos', 'emails', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# OBS: O método fromkeys recebe dois parametros: um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)