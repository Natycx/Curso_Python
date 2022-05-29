"""
Utilizamos o try/except para tratar erros que podem ocorrer no nosso programa.
Prevenindo que o programa pare de funcionar e o usuario receba mensagens de erro


# Exemplo 1 - Tratando um erro generico

try:
    geek()
except:
    print('Deu algum problema')

# Exemplo 3

try:
    len(5)
except TypeError:
    print('Vc está utilizando uma função inexistente')

# Exemplo 4

try:
    len(5)
except TypeError as err:
    print(f'Gerou o seguinte error {err}')

    # Exemplo 5

try:
    len(5)
except TypeError as erra:
    print(f'Deu erro {erra}')
except NameError as errb:
    print(f'Deu erro {errb}')
except:
    print('Deu um erro diferente')


"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {"nome": "Geek"}
print(pega_valor(dic, "game"))