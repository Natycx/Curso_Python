"""
Reversed:

OBS: Não confunda com a função reverse()

A Função reversed() retorna um iteravel chamado Reverse Iterator
"""
# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retorna para uma lista, tupla ou conjunto

print(list(reversed(lista)))

print(tuple(reversed(lista)))

print(set(reversed(lista)))

for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')
# Podemos Fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Ja vimos como fazer isso mais facil com slice de strings
print('Geek University'[::-1])

for n in reversed(range(0, 10)):
    print(n)

for n in range(9, -1, -1):
    print(n)