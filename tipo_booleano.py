"""
tipo Boolean

algebra booleana criada por george boole

2 constante, verdadeiro ou falso

true -> Verdadeiro
false -> False

OBS: sempre com a inicial maiúscula

errado :
true, false

Certo :
True, False

"""

ativo = True

print(ativo)

"""
Operações basics:
"""

# Negação (not)
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre o contrario.
"""
print(not ativo)

logado = False

# Ou (or):
"""
É uma operação binaria, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro
True or True = True
True or False = True
False or True = True
False or False = False
"""
print(ativo or logado)

# E (and)
"""
Também é uma operação binaria, ou seja, depende de dois valores. Ambos
os valores devem ser verdadeiro
True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""