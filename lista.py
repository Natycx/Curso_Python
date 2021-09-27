"""
Listas

listas em python funciona como vetores/matrizes (arrays) em outras linguagens,
com a diferença de serem dinamicos e também de podermos colocar qualquer tipo de dado

linguagens C/Java: arrays
    - Possuem tamanha e tipo de dado fixo:
    Ou seja, nestas linguagens se vc criar um array do tipo int e com tamanho 5
    , este array será sempre do tipo inteiro e poderá ter sempre no maximo 5 valores

Já em python
- dinamico: não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- qualquer tipo de dado: Não possuem tipo de dado fixo; ou seja podemos colocar qualquer tipo de dados

As listas em python são representadas por colchetes: []

Listas são mutáveis

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

lista6 = ['Programação', 'em', 'Python: ', 'Essencial']


# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if 8 in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

if 'e' in lista5:
    print('Encontrei a letra e')
else:
    print('Não encontrei a letra e')

# Podemos ordenar uma lista
lista1.sort()
print(lista1)

# Podemos contar o numero de ocorrência de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elementos em lista, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: com append, nos só conseguimos adicionar 1 elemento por vez
lista1.append([8, 3, 1]) # coloca a lista como elemento unico (sublista)
print(lista1)

lista1.extend([123, 44, 67])  # não aceita valor unico
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas

lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista
# Forma 1
lista1.reverse()
lista2.reverse()

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista2))

# Podemos remover o ultimo elemento de uma lista
# OBS: O pop não somente remove o ultimo elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# Os elementos á direita desse índice serão deslocados para a esquerda.
# Se não houver elemento no índice informado, teremos o erro IndexError.


lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# podemos converter uma string para uma lista

# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS : Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string

curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca $ entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista7 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]
print(lista7)

# Iterando sobre listas

# Exemplo 1

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - utilizamos while

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair')
    produto= input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# utilizamos variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pense na lista como uma roda
# onde o final de um elemento está ligado ao inicio da lista
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])
# print(cores[-5]) # Erro, pois não existe indice - 5


cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

cores = ['verde', 'amarelo', 'azul', 'branco']
# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)


# Outros métodos não tão importantes mas também úteis

# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# em qual indice da lista esta o valor 6
print(numeros.index(6))

# em qual indice da lista esta o valor 9
print(numeros.index(9))

# OBS: Caso não tenha esse elemento na lista, será apresentado erro ValueError
# print(numeros.index(19))

print(numeros.index(5))  # retorna o indice do primeiro elemento encontrado

# podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # buscamos a partir do índice 1
# print(numeros.index(5, 2))  # buscamos a partir do índice 2
# print(numeros.index(5, 3))  # buscamos a partir do índice 3
# print(numeros.index(5, 4))  # buscamos a partir do índice 4

# OBS: Caso não tenha esse elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # buscar o indice do valor 8,  entre os indices 3 a 6


# Revisar slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:])  # iniciando do indice 1 e pegando todos os elementos restante

# trabalhando com slice de lista com o parametro 'fim'

print(lista[:2])  # começa em 0, pega até o índice 2 - 1
print(lista[:4])  # começa em 0, pega até o indice 3 - 1
print(lista[1:3])  # começa em 1, pega até o indice 3 - 1

# trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2])  # Começa em 1, e vai até o final de 2 em 2

print(lista[::2])  # começa em 0, vai até o final de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes [1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

# Soma, valores maximos, valores minimos, tamanho

# se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # maximo valor
print(min(lista))  # minimo valor
print(len(lista))  # tamanho da lista

# transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de lista

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: se tivermos mais elementos para desempacotar do que variaveis
# para receber os valores, teremos ValueError

# Copiando uma lista para outra(Shallow copy e deep copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]

nova = lista.copy()

print(nova)
nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista
# não afeta a outra. Isso em python é chamado de Deep Copy(copia profunda)

# forma 2 - shallow copy
lista = [1, 2, 3]
print(lista)

nova = lista  # copia
print(nova)

nova.append(4)
print(lista)
print(nova)

# Vejamos que utilizamos a copia via atribuição e copiamos os dados da lista
# para a nova lista, mas após realizar modificação se refletiu em ambas as listas
# isso em python é chamado de shallow copy

"""