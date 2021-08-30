import math

A = float(input("Digite o angulo "))
R = A * math.pi/180
print(R)

# 2

R = float(input("Digite o angulo "))
A = R * 180/math.pi
print(A)

# 3

P = float(input('Digite o valor em polegadas '))
C = P * 2.54
print(f'Valor em centimetres {C}')

# 4

C = float(input('Digite o valor em centímetros '))
P = C / 2.54
print(f'Valor em polegadas {P}')

# 5

M = float(input('Digite o valor em metros '))
L = 1000 * M
print(f'O valor em litros é {L}')

# 6

L1 = float(input('Digite o valor em litros '))
M1 = L1 / 1000
print(f'O valor em metros é {M1}')

# 7

K = float(input('Digite o valor em KG'))
L2 = K / 0.45
print(f'O valor em libras é {L2}')

# 8

L3 = float(input('Digite o valor libras '))
K = L3 * 0.45
print(f'O valor em KG é {K}')