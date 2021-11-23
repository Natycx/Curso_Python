"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia á
Teoria dos conjuntos da Matemática.

- Aqui no Python, os conjuntos são chamados de sets

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos e dicionarios em python:
    - Um dicionario tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente
# o mesmo será ignorado sem gerar error e não fará parte do conjunto

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

lista = [99, 2, 34, 23, 2,12, 1, 44, 5, 34]
print(f'Lista : {lista} com {len(lista)}')

tupla = (99, 2, 34, 23, 2,12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)}')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)}')

conjunto = {99, 2, 34, 23, 2,12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)}')

# Assim como todo outro conjunto Python podemos colocar todos os tipos de dados
# misturados em sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine um formulario de cadastro de visitantes em uma feira ou museu
# e os visitantes informaram manualmente a cidade de onde vieram

# Adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['Belo Horizonte', 'São paulo', 'Campo Grande', 'São paulo', 'Campo Grande', 'Cuiaba', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos.

# podemos utilizar o set para isso:
print(len(set(cidades)))

# Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4)  # A duplicidade n gera erro, ela é ignorada

print(s)

# Remover um elemento do conjunto

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)  # Não é indice, informamos o valor a ser removido

print(s)

# Forma 2

s.discard(2)
print(s)

s = {1, 2, 3}
# Copiando um conjunto para outro

# Forma 1 - Deep copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shalow copy

novo = s

novo.add(4)

print(novo)
print(s)

s = {1, 2, 3}
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Precisamos gerar um conjuntos com nomes de estudantes únicoss

# Metodos Matematicos de conjuntos

# Temos dois conjuntos: um contendo estudantes do curso Python
# e um contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Gerar um conjunto de estudantes que não estão em dois cursos

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Utilizando 2 - Utilizando o caracter o pipe |
unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Veja que alguns alunos que estudam python também estudam Java.

# Gerar um conjunto de estudantes que estão em ambos os cursos

# forma 1 - utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)

print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java

print(ambos2)

"""

# Soma*, valor maximo*, valor minimo*, tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))




