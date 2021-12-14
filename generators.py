"""
Generators

- Tuple comprehension se chama generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C for nome in nomes] ))

# Utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator

res = (nome[0] == 'C' for nome in nomes)

print(type(res))
print(res)


# Qual é a utilidade de getsizeof()? Retorna a quantidade de bytes em memoria do elemento passado como parametro

from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memoria. Quanto maior a string mais espaço ocupa

print(getsizeof('Geek'))
print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(True))

print(getsizeof(5468489446465188))

from sys import getsizeof

# Gerando uma lista de numeros com list comprehension

list_comp = getsizeof([x * 10 for x in range(100)])

# Gerando uma lista de numeros com set comprehension

set_comp = getsizeof({x * 10 for x in range(100)})

# Gerando uma lista de numeros com dic comprehension

dic_comp = getsizeof({x:x * 10 for x in range(100)})

# Gerando uma lista de numeros com generator

gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memoria')
print(f'List Comprehension{list_comp}')
print(f'Set Comprehension{set_comp}')
print(f'Dic Comprehension{dic_comp}')
print(f'Generator {gen}')


"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))

for num in gen:
    print(num)