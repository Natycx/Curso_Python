"""
Definindo funções

- Funções são pequenos trechos de códigos que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos imilares por repetidas vezes;


OBS: se vc escrever uma função que realiza varias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada

já utilizamos varias funções desde que iniciamos este curso

print()
len()
max()
min()
count()
e muitas outras


# Exemplo de utilização de funções;

cores = ['verde', 'amarelo', 'azul', 'branco']

# utilizamos a função integrada (Built - in) do python print()

print(cores)

curso = "Programação em puthon: Essencial"

print(curso)

cores.append('roxo')

cores.clear()
print(cores)

# print(help(print))

# DRY - Don't repeat yourself - não repita seu codigo


"""


# Como definir funções:

"""
Em Python a forma geral de definir uma função é:

def nome_da_funcao(parametros):
    bloco_da_funcao
    
    
"""


def diz_oi():
    print('oi!')

"""
OBS: 
1 - dentro de uma função podemos utilizar outras funções;
2 - veja que nossa função só executa 1 tarefa, ou seja, a unica coisa que ela faz é 
dizer oi
3 - veja que esta função n recebe nenhum parametro de entrada;
4 - vejamos que esta função n retorna nada

"""

# Utilizando funções

# Chamada de execução
# diz_oi()

# Exemplo 2


def cantar_parabens():
    print('Parabens pra vc')
    print('Nessa data querida')
    print('Muitas felicidade')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


# for n in range(5):
#   cantar_parabens()


# Em puthon, podemos incluisive criar variaveis do tipo de uma função e executar esta função
# atraves da variavel

canta = cantar_parabens

canta()