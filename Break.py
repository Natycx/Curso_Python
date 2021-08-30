"""
Saindo de Loops com break

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneiras projetadas.

"""
# Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sair do loop')

# Exemplo 2

while True:
    comando = input('Digite sair para terminar o loop ')
    if comando == 'sair':
        break

