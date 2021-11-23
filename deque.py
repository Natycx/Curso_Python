"""
Modulo Collection - Deque

Podemos dizer qe o deque é uma lista de alta performance



"""

# Importando

from collections import deque

deq = deque('geek')

print(deq)

# Acidionando elementos no deque

deq.append('y')  # adiciona no final

print(deq)

deq.appendleft('k')  # adiciona no começo da lista

print(deq)

# Remover elementos

print(deq.pop())  # remove e retorna o ultimo elemento

print(deq)

print(deq.popleft())

print(deq)