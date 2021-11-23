"""
Modulo Collection: Ordered Dict

# Em um dicionario a ordem de inserção não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

for chave, valor in dicionario.items():
    print(f'Chave = {chave}, Valor = {valor}')


OrderedDict é um dicionario que nos garante a ordem de inserção dos elementos.


# Fazendo import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

"""
from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)