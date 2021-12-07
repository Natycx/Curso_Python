"""
Entendendo o *args

- O *args é um parametro como outro qualquer, Isso significa que vc poderá chamr
de qualquer coisa desde que começe com asteristico

Exemplo:
*xis

Mas por convenção *args para defini- lo

mas o q é o *args?

O parametro *args utilizado em uma função coloca os valores extras informados
como entrada em uma tupla então desde já lembre - se que tuplas são imutaveis.

# Exemplos


def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

# Entendendo o args


def soma_todos_numeros(nome, sobrenome, *args):
    return sum(args)


print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3, 4))
print(soma_todos_numeros('Angelina', 'Jolie', 3, 4, 5, 6))

# Outros exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem - vindo Geek!'
    return 'Eu não tenho certeza quem é vc'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.154))

"""


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numero = [1, 2, 3, 4, 5, 6, 7]

#print(soma_todos_numeros(numero))  # TypeError, ele da erro ao utilizar listas, pois
# ele cria uma lista com 1 elemento ([1, 2, 3, 4, 5, 6, 7])

# Desempacotador

print(soma_todos_numeros(*numero))

# OBS: O asteristico serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados.
# desta forma ele saberá que precisará antes desempacotar esses
# dados

