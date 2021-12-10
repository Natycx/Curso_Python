"""
Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são
funções sem nome, ou seja, funções anonimas

# Função em python

def soma(a,b):
    return a + b


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Expressão Lambda

lambda x: 3 * x + 1

# Como utilizar a expressão lambda

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo('             FELICITY     ', '  jones'))

# Em funções python podemos ter nenhuma ou varias entradas. em lambdas tbm

amar = lambda : 'como n amar python? '
uma = lambda x: 3 * x + 1
duas = lambda x,y: (x * y) ** 0.5
tres = lambda x,y,z: 3 /(1 / x + 1 / y + 1 / z)

print(amar)
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke',
           'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells',
           'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)


"""

# função quadratica
# f(x) = a * x ** 2 + b * x +c


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * +c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 2)(2))
# Viado
# abc