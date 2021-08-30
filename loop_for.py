"""
Loop for

Loop -> Estrutura de repetição
for -> Uma dessas estrutura

python
for item in interavel:
    //execução do loop

utilizamos loops para iterar sobre sequencias ou valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
-Range
    numeros = range(1, 10)

# Exemplo 1(iterando uma string)

for letra in nome:
    print(letra)

# Exemplo de for 2(iterando sobre uma lista)

for numero in lista:
    print(numero)


range (valor_inicial, valor_final)
OBS: o valor final não é inclusive
1
2
3
4
5
6
7
8
9
10 - Não inclui

# Exemplo 3(iterando sobre um range)
for numero in range(1, 10):
    print(numero)

Enumerate:
(0, 'G'), (1, 'e'), (2, 'e'), (3, 'k')...

for i, v in enumerate(nome):
    print(nome[i])

for _, letra in enumerate(nome):
    print(letra)
Obs: quando não precisamos de um valor, podemos descarta-lo utilizando um (_)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)  # temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

quantidade = int(input('Quantas vezes o lup deve rodar '))
soma = 0

for n in range(1, quantidade + 1):
    num = int(input(f'Informe o {n}/{quantidade} valor: '))
    soma += num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')
Tabela de emojis https://apps.timwhitlock.info/emoji/tables/unicode

"""

# Original U+1F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
