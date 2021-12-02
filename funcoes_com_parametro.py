"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

Se a gente pensar em uma função, já sabemos que temos funções que:

- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# refatorando uma função


def quadrado(numero):
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

# Refatorando a função


def cantar_parabens(aniversariante):
    print('Parabens pra vc')
    print('Nessa data querida')
    print('Muitas felicidade')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')


cantar_parabens('Marcos')

# Funções podem ter inumeros parametros, eles são separados por virgulas

def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, "Geek "))
print(outra(5, 4, "Python "))


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))

# A diferença entre parametros e argumentos

# parametros são variaveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função

# a ordem dos parametros importa

# Caso utlizamos nomes dos parametros nos argumentos para informa-los
# podemos utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(sobrenome='Garcia', nome='Natalia'))

"""
# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))