"""
Funções com Parametro Padrão (default paramters)

- funções onde a passagem de parametro seja opcional
# Exemplo de função onde a passagem de parametro seja opcional
print('Geek University')

print()

# Exemplo de função onde a passagem de parametro é obrigatorio

def quadrado (numero):
    return numero ** 2


print(quadrado(3))
print(quadrado())

def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuario


# OBS
# Se o usuario passar somente 1 parametro este sera atribuido ao parametro numero
# e sera calculado o quadrado deste numero;
# se o usuario passar 2 argumentos o primeiro sera atribuido ao parametro numero
# e o segundo ao parametro potencia

# Em funções python, os parametros com valores padrão DEVEM sempre esta no final
# da declaração

# ERRO
def teste(num=2, potencia):
    return num**potencia

print(teste())

# Outros exemplos

def soma(num1=5, num2=4):
    return num1 + num2


print(soma(4, 5))

print(soma(4))
print()

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que vc era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())

print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stefany'))

# Pq utulizar parametros com valores default
- Nos permite ser mais flexiveis nas funções
- Evita erros com parametros incorretos;
- Nos permite trabalhar com exemplos mais legiveis de codigo

# quais tipos de dados podemos utilizar com valores default para parametros?

- Qualquer tipo de dado:
    - numeros, strings, floats, listas, tuplas, dic, funcoes e etc

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 3, subtracao))


# Escopo- Evitar problemas e confusões

# Variavel global
# Variavel local

instrutor = 'Geek'  # Variavel global

def diz_oi():
    instrutor = 'Python'
    return f'Oi {instrutor}'

# Obs: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local tera preferencia

def diz_oi():
    prof = 'Geek'  # Variavel local
    return f'Olá {prof}'

print(diz_oi())
print(prof)

# Atenção com variaveis globais (se puder evitar evite)
total = 0


def incrementa():
    total = total + 1  # UnboundLocalError
    return total

print(incrementa())


"""

# Atenção com variaveis globais (se puder evitar evite)
total = 0


def incrementa():
    global total   # Avisando que queremos utilizar a variavel global
    total = total + 1
    return total

print(incrementa())

#  podemos ter funções que são declaradas dentro de funções
# e tbm tem uma forma especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador+1
        return contador
    return dentro()