"""
Recebendo dados usuário

input() -> todo dado recebido via input é tipo string

Tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplo:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas ->'''Angelina Jolie '''
"""
# - Aspas duplas triplas ->"""Angelina Jolie """

# Entrada de dados
# print("Qual seu nome? ")
# nome = input()   # Input -> Entrada

nome = input('Qual seu nome? ')

# Exemplo de print antigo 2.x
# print("Seja bem vindo(a) %s" % nome)

# Exemplo de print moderno 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print mais atual 3.7
print(f"Seja bem vindo(a) {nome}")

# print("Qual a sua idade? ")
# idade = input()

idade = int(input('Qual a sua idade? '))


# processamento

# Saida de dados
# Exemplo de print antigo 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print moderno 3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print mais atual 3.7
print(f'A {nome} tem {idade} anos')

print(f'A {nome} nasceu em {2021 - idade}')

