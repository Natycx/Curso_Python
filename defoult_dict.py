"""
Modulo Collection - Defoult Dict


dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

Defoult Dict -> Ao criar um dicionario utilizando-o nos informamos um valor default
podendo utilizar um lambda para isso. este valor será utilizado sempre
que não houver um valor definido. Caso tentemos acessar uma chave que não existe essa chave
será criada e o valor default será atribuido

OBS: Lambdas são funções sem nome. que podem ou não receber parametrosss
de entrada e retornar valores

"""

# Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['cuso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro'])  # Não dará erro

print(dicionario)