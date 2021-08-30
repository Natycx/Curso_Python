""""
class Calculadora:
    pass


class CalculadoraCientifica:
    pass


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5


if 'a' in 'banana1':
    print('tem')

# Import errado

import sys , os

# Import certo

import sys
import os

# Não há problemas em utilizar:

from types import StingType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imporsts devem ser colocados no topo do arquivo, logo depois de quaisquer
# comentarios ou docstrings e antes de constantes ou variaveis globais

# não faça

funcao( algo[ 1 ], { outro : 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça

algo (1)

# Faça:

algo(1)

# n faça:

disc ['chave'] = list [indice]

# faça

dict['chave'] = lista[indice]

# n faça

x                           = 1
y                           = 3
variavel_longa = 5

# Faça

x = 1
y = 3
variavel_longa = 5


"""

