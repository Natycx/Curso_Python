"""
Módulo Collection - counter

High performance Container Datetypes

Counter -> recebe um iteravel como parametro e cria um objeto do tipo
Collection counter que é parecido como um dicionario, contendo como chave o elemento
da lista passada como parametro e como valor a quantidade de ocorrencias desse elemento


# Utilizando o Counter

from collections import Counter

# Podemos utilizar qualquer iteravel
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 1, 1, 2, 2, 4, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 1, 1, 2, 2, 4, 5, 5, 3, 45, 45, 66, 66, 43, 34])

# Veja que para cada elemento da lista o counter criou uma chave e colocou como valor a quantidade de ocorrencia

from collections import Counter

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""
from collections import Counter

texto = """Annelies Marie Frank foi uma adolescente alemã de origem judaica, vítima do Holocausto. Tornou-se uma das 
figuras mais discutidas da história 
após a divulgação póstuma do Diário de Anne Frank (1947), no qual documentou suas experiências enquanto vivia escondida 
em cômodos ocultos de uma empresa durante a ocupação 
alemã nos Países Baixos na Segunda Guerra Mundial. Desde então, passou a ser referida como um "símbolo da luta contra o 
preconceito" e teve sua história servindo como base para 
diversas peças de teatro e filmes ao longo dos anos. Em 1999, 
foi contemplada como uma das pessoas mais importantes do século XX em uma lista organizada pela revista Time."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))