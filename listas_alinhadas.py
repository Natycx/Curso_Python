"""
LIstas aninhadas(Nested Lists)

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - unidimensionais (arraus/ vetores);
    - Multidimensinais (Matrizes);

Em Python nos temos as listas

numeros = [1, 2, 3, 4, 5]
# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas)

# como fazemos para acessar os dados?

print(listas[0][1])
print(listas[2][1])

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)


# list Comprehension
[[print(valor) for valor in lista]for lista in listas]


"""
# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])
