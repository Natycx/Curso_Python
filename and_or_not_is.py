"""
Estruturas Lógicas: and(e), not(Não), is(é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False
se for False vira true
Para o 'is', é usado em comparação

"""
ativo = True
logado = False

if ativo:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar a sua conta. Por favor, cheque seu e-mail')

if ativo or logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar a sua conta. Por favor, cheque seu e-mail')

# Se não estiver ativo
if not ativo:
    print('Você precisa ativar a sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem vindo usuário')

# print(not False)

if ativo is True:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar a sua conta. Por favor, cheque seu e-mail')

# ativo é True?
print(ativo is False)
