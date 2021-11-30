"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é none

OBS: Funções Python que retornam valores, devem retornar estes valores com
a palavra reservado return

OBS: Não precisamos necessariamente criar uma varialvel para
receber o retorno de uma função. Podemos passar a execução da fun;cão para
outras funções

# Refatorando a função


def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira função


def diz_oi():
    return 'Oi'


print(diz_oi())

alguem = ' Pedro!'

print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja ela sai da execução da função
2 - Podemos ter em uma função diferentes returns
3 - Podemos em uma função retornar qualquer tipo de dados e até mesmo
multiplos valores;


def diz_oi():
    return 'Oi '
    print('uhsdiuhsiuai')  # Não executa

print(diz_oi())

# Exemplo 2


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Exemplo 3


def outra_funcao():
    return 2, 3, 4, 5

# num1, num2, num3, num5 = outra_funcao()
# print(num1, num2, num3, num5)


print(outra_funcao())


# Função para jogar a moeda

from random import random


def joga_moeda():
    # Gera um numero randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

"""


def e_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False


print(e_impar())
