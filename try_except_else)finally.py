"""
Try/ Except / Else / Finally

Dica de quando e onde tratar o codigo:

Toda entrada do usuário deve ser tratada!

# Else só é executado somente se não ocorrer o erro

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# FInally

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('vc não digitou um valor valido.')
else:
    print(f'Vc digitou o numero {num}')
finally:
    print('Executando o finally')

# O bloco finally é sempre executado. Independente se houve a exceção ou n

# O finally, geralmente é utilizado para fechar ou deslocar recurso


def dividir(a, b):
    try:
        return int(a)/int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por 0'


num1 = (input('Informe o primeiro numero: '))
num2 = (input('Informe o segundo numero: '))

print(dividir(num1, num2))
# Generico
def dividir(a, b):
    try:
        return int(a)/int(b)
    except:
        return 'O correu um problema'


num1 = (input('Informe o primeiro numero: '))
num2 = (input('Informe o segundo numero: '))

print(dividir(num1, num2))
"""


def dividir(a, b):
    try:
        return int(a)/int(b)
    except(ValueError, ZeroDivisionError):
        return 'O correu um problema'


num1 = (input('Informe o primeiro numero: '))
num2 = (input('Informe o segundo numero: '))

print(dividir(num1, num2))
