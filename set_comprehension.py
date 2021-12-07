"""
Set comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

"""

# Exemplos

numero = {num for num in range(1, 7)}
print(numero)

# Outro exemplo

numero = {x ** 2 for x in range(10)}
print(numero)

# Desafio: Faça uma alteração na estrutura acima para gerar um dicionario ao inves de set

numero = {x: x ** 2 for x in range(10)}
print(numero)

# Para finalizar

letras = {letras for letras in 'Geek University'}
print(letras)