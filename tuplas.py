"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças basicas:

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla

# Cuidado: as tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidado 2: Tupla com 1 elemento

tupla3 = (4)  # Isso não é uma tupla
print(tupla3)

print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# Podemos concluir que tuplas são definidas pela virgula e não pelo parenteses

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinamicamente com o range(inicio,fim,passo)

tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial ')
escola, curso = tupla
print(escola)
print(curso)

# OBS: ValueError se colocarmos um numero diferente de elementos para desempacotar.

# Métodos para: adição, remoção de elementos nas tuplas não existem, dado o fato dado o fato das tuplas serem imutáveis

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(tupla1)
print(tupla2)
print(tupla1 + tupla2)  # Tupas são imutavais
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Tuplas são imutaveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)


# Iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

escola = tuple('Geek University')
print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com whie
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice um elemento está na tupla
print(meses.index('Junho'))

# OBS: Caso o elemento não exista, será gerado erro

# print(meses.index('Playstation'))

meses = ('Janeiro', 'Fevereiro', 'Março', 'abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Slicing

# tupla[Inicio:fim:passo]

print(meses[5:9])

# Por quê utilizar tuplas?

# Tuplas são mais rapidas do que listas.
# Tuplas deixam seu codigo mais seguro
# isso porque trabalhar com elementos imutavais traz segurança para o codigo


"""
# copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla
print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(tupla)


