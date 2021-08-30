"""
Loop wile
Forma geral

while expressão_boolean:
    //execução do loop

O bloco do wile será repetido enquanto a expressão boolean for verdadeira

Expressão Boolean é toda expressão onde o resultado é verdadeiro ou falso

exemplo:

num = 5

num < 5

Exemplo
num = 1

while num < 10:
    print(num)
    num = num + 1

# Em um loop while, é importante que cuidemos do criterio de parada

"""
resposta = ''

while resposta != 'sim':
    resposta = input('Ja acabou Jessica? ')