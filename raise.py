"""
Levantando os proprios erros com raise

raise -> Lança exceções

OBS: raise é uma palavra reservada, assim como def




"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor is not cores:
        raise ValueError (f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'preto')
