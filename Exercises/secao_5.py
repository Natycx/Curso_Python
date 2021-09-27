import math
import random


def maior():
    valor = []
    for _ in range(2):
        x = int(input('Digite o valor: '))
        valor.append(x)
    print(max(valor))


def positivo_negativo():
    x = int(input("Digite um numero: "))
    if x > 0:
        print(math.sqrt(x))
    else:
        print('Esse numero é invalido!')


def numero_real():
    x = int(input('Digite um numero: '))
    if x > 0:
        print(math.sqrt(x))
    else:
        print(x ** 2)


def positivo():
    x = int(input('Digite o numero: '))
    if x > 0:
        print(f'{x ** 2} ,{math.sqrt(x)}')
    else:
        print('O numero é invalido!')


def par_ou_impar():
    x = int(input())
    if x % 2 == 0:
        print('Esse numero é par!')
    else:
        print('Esse numero é impar!')


def maior_menor():
    valor = []
    for _ in range(2):
        x = int(input('Digite o valor: '))
        valor.append(x)
    print(f'{max(valor)}, {max(valor) - min(valor)}')


def maxvalor():
    valor = []
    for _ in range(2):
        x = int(input('Digite o valor: '))
        valor.append(x)
    if valor[0] == valor[1]:
        print('Valores iguais!')
    else:
        print(max(valor))


def notas():
    notas = []
    for _ in range(2):
        x = float(input('Digite a nota do aluno: '))
        if x < 0:
            print('Nota invalida!')
        else:
            notas.append(x)
    media = (notas[0] + notas[1]) / 2
    print(media)


def salario():
    salario = float(input('Digite o salario: '))
    emprestimo = float(input('Digite o valor da prestacão: '))
    porcentagem = (100 * emprestimo) // salario
    if porcentagem > 20:
        print('Emprestimo negado!')
    else:
        print('Emprestimo concedido!')


def peso_ideal():
    altura = float(input('Digite a altura: '))
    sexo = input('Digite o sexo da pessoa: ')
    if sexo == 'masculino':
        homem = (72.7 * altura) - 58
        print(homem)
    elif sexo == 'feminino':
        mulher = (62.1 * altura) - 44.7
        print(mulher)


def logaritmo():
    x = int(input('Digite um numero: '))
    if x < 0:
        print('Numero invalido!')
    else:
        print(math.log(x))


def media():
    nota = []
    for _ in range(3):
        x = float(input('Digite as notas: '))
        nota.append(x)
    media = (nota[0] + nota[1] + (nota[2] * 2)) / 4
    print(media)


def exame():
    trabalho = float(input('Digite a nota do trabalho: '))
    avaliacao = float(input('Digite a nota da avaliacao: '))
    exame = float(input('Digite a nota do exame: '))
    soma = trabalho + avaliacao + exame
    if soma < 3:
        print('Reprovado!')
    elif soma < 5:
        print('Em recuperação!')
    else:
        print('Aprovado!')


def semana():
    dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']
    semana = int(input('Digite o dia da semana em numeros: '))
    print(dias[semana - 1])


def mes():
    mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
           'Outubro', 'Novembro', 'Dezembro']
    x = int(input('Digite o mês em numero: '))
    print(mes[x - 1])


def area_trapezio():
    basemaior = float(input('Digite a base maior: '))
    basemenor = float(input('Digite a base menor: '))
    altura = float(input('Digite a altura: '))
    area = ((basemaior + basemenor) * altura) / 2
    print(area)


def operacoes_matematicas():
    menu = ['Soma', 'Diferença', 'Multiplicação', 'Divisão']
    print(menu)
    operacoes = input('Digite a operação matematica: ')
    if operacoes == 'soma':
        x = int(input('Digite o numero para somar : '))
        print(f'A soma de {x} + {x} = {x + x}')
    elif operacoes == 'diferença':
        x = int(input('Digite o numero para diminuir : '))
        print(f'A soma de {x} - {x} = {x - x}')
    elif operacoes == 'multiplicação':
        x = int(input('Digite o numero para multiplicação : '))
        print(f'A soma de {x} * {x} = {x * x}')
    elif operacoes == 'divisão':
        x = int(input('Digite o numero para dividir : '))
        print(f'A soma de {x} / {x} = {x / x}')


def divisivel():
    x = int(input('Digite o numero a ser verificado: '))
    if x % 3 == 0:
        print('Esse numero é divisivel por 3')
    elif x % 5 == 0:
        print('Esse numero é divisivel por 5: ')
    else:
        print('Esse numero não é divisivel nem por 3 nem por 5!')


def triangulos():
    lados = []
    for _ in range(3):
        x = float(input('Digite os lados do triangulo: '))
        lados.append(x)
    if lados[0] < lados[1] + lados[2] and lados[1] < lados[0] + lados[2] and lados[2] < lados[0] + lados[1]:
        print('Pode ser um triangulo!')
        if lados[0] == lados[1] == lados[2]:
            print('Triangulo equilatero')
        elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
            print('Triangulo isósceles')
        else:
            print('Triangulo escaleno')
    else:
        print('Não pode ser um triangulo!')


def menu():
    menu = ['Soma', 'Diferença', 'Multiplicação', 'Divisão']
    print(menu)
    numeros = [int(input('Digite o numero: ')) for _ in range(2)]
    operacoes = input('Digite a operação matematica: ')
    if operacoes == 'soma':
        print(f'{numeros[0] + numeros[1]}')
    elif operacoes == 'diferença':
        print(f'{max(numeros) - min(numeros)}')
    elif operacoes == 'multiplicação':
        print(f'{numeros[0] * numeros[1]}')
    elif operacoes == 'divisão':
        print(f'{numeros[0] / numeros[1]}')


def aposentadoria():
    idade = int(input('Digite a idade: '))
    tempo_de_sevirco = int(input('Digite o tempo de serviço: '))
    if idade >= 65:
        print('Pode se aposentar!')
    elif tempo_de_sevirco >= 30:
        print('Pode se aposentar!')
    elif idade >= 60 and tempo_de_sevirco >= 25:
        print('Pode se aposentar!')
    else:
        print('Não pode se aposentar!')


def bissexto():
    ano = int(input('Digite o ano que vc gostaria de saber: '))
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        print('O ano é bissexto')
    else:
        print('O ano não é bissexto!')


def estados():
    produto = int(input('Digite o valor do produto: '))
    estado = input('Digite o estado: ')
    if estado == 'MG':
        preco = produto + ((produto * 7) / 100)
        print(f'O valor final do produto é {preco}')
    elif estado == 'SP':
        preco = produto + ((produto * 12) / 100)
        print(f'O valor final do produto é {preco}')
    elif estado == 'RJ':
        preco = produto + ((produto * 15) / 100)
        print(f'O valor final do produto é {preco}')
    elif estado == 'MS':
        preco = produto + ((produto * 8) / 100)
        print(f'O valor final do produto é {preco}')
    else:
        print('Estado invalido!')


def equacao():
    a = int(input())
    b = int(input())
    c = int(input())
    if a != 0:
        delta = (b ** 2) - (4 * a * c)
        if delta < 0:
            print('Não existe raiz')
        else:
            equacao1 = (- b + math.sqrt(delta)) / (2 * a)
            equacao2 = (- b - math.sqrt(delta)) / (2 * a)
            if delta == 0:
                if equacao1 != 0:
                    print(equacao1)
                elif equacao2 != 0:
                    print(equacao2)
            elif delta >= 0:
                print(equacao1, equacao2)

    else:
        print('Não pode ser equação do segundo graus')


def litros():
    distancia = float(input('Digite a distancia pecorrida: '))
    litros = float(input('Digite a quantidade de litros gastos '))
    consumo = distancia / litros
    if consumo < 8:
        print('Venda o carro!')
    elif consumo < 14:
        print('Economico!')
    else:
        print('Super economico!')


def idade():
    idade = int(input("Digite a idade do nadador: "))
    if 5 <= idade <= 7:
        print('Categoria Infantil A')
    elif 8 <= idade <= 10:
        print('Categoria Infantil B')
    elif 11 <= idade <= 13:
        print('Categoria Juvenil A')
    elif 14 <= idade <= 17:
        print('Categoria Juvenil B')
    elif idade >= 18:
        print('Categoria senior')


def medias():
    a = int(input())
    b = int(input())
    c = int(input())
    print('(a) Geometrica (b) Ponderada (c) Harmonica(d) Aritmetica')
    x = input('Digite a opção de media: ')
    if x == 'a':
        print(pow((a * b * c), 1 / 3))
    elif x == 'b':
        print((a + 2 * b + 3 * c) / 6)
    elif x == 'c':
        print(1 / (1 / a + 1 / b + 1 / c))
    elif x == 'd':
        print((a + b + c) / 3)


def prova():
    acertos = 0
    for _ in range(5):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        soma = a + b
        print(f'Qual a soma de {a} + {b}')
        x = int(input())
        if soma == x:
            print('Acertou')
            acertos = acertos + 1
    print(f'Você acertou {acertos} perguntas!')


def ordem_crescente():
    valores = [int(input()) for _ in range(3)]
    valoresmin = min(valores)
    valormax = max(valores)
    valores.remove(valormax)
    valores.remove(valoresmin)
    print(valoresmin, valores, valormax)


def classificacao_peso():
    altura = float(input('Digite a altura: '))
    peso = float(input('Digite o peso: '))
    if altura < 1.20:
        if peso <= 60: print('Categoria A')
        elif 60 > peso <= 90: print('Categoria G')
        else: print('Categoria G')
    elif 1.20 < altura >= 1.70:
        if peso <= 60: print('Categoria B')
        elif 60 > peso <= 90: print('Categoria E')
        else: print('Categoria H')
    else:
        if peso <= 60: print('Categoria C')
        elif 60 > peso <= 90: print('Categoria F')
        else: print('Categoria I')


def pedidos():
    total = 0
    while True:
        print('Cachorro quente: 100 : R$ 1.20 \n Bauru simples: 101 : R$ 1.30 \n Bauru com ovo: 102 : R$ 1.50 \n '
              'Hamburguer: 103 : R$ 1.20 '
              '\n Cheeseburguer: 104 : R$ 1.70 \n Suco: 105 : 2.20 \n Refrigerante: 106 : R$ 1.00')
        codigo = int(input('Digite o codigo do produto: '))
        quantidade = int(input('Digite quantidade do pedido: '))
        preco = 0
        if codigo == 100: preco = quantidade * 1.20
        elif codigo == 101: preco = quantidade * 1.30
        elif codigo == 102: preco = quantidade * 1.50
        elif codigo == 103: preco = quantidade * 1.20
        elif codigo == 104: preco = quantidade * 1.70
        elif codigo == 105: preco = quantidade * 2.20
        elif codigo == 106: preco = quantidade * 1.00
        total = total + preco
        continuacao = input('Deseja escolher mais algum item? ')
        if continuacao == 'não': break
    print(f'O total da compra foi {total}')


def mudanca():
    preco = float(input('Digite o valor do produto: '))
    if preco < 50:
        print(f'Barato')
    elif 50 <= preco <= 100:
        novo_preco = (preco * 10 / 100) + preco
        if novo_preco < 80: print('Barato!')
        elif 80 <= novo_preco <= 120: print('Normal')
    else:
        novo_preco = (preco * 15 / 100) + preco
        if 80 <= novo_preco <= 120: print('Normal')
        elif 120 < novo_preco <= 200: print('Caro')
        else: print('Muito caro')


def faltas():
    nota = float(input('Digite a nota do aluno: '))
    faltas = int(input('Digite o numero de faltas: '))
    if 9 <= nota <= 10:
        if faltas >= 20: print('Sua nota agora está entre 7.5 e 8.9, conceito B')
        else: print(f'Sua nota é {nota}')
    elif 7.5 <= nota < 9:
        if faltas >= 20: print('Sua nota agora está entre 5 e 7.4, conceito C')
        else: print(f'Sua nota é {nota}')
    elif 5 <= nota < 7.5:
        if faltas >= 20: print('Sua nota agora está entre 4.0 e 4.9, conceito D')
        else: print(f'Sua nota é {nota}')
    elif 4 <= nota < 5:
        if faltas >= 20: print('Sua nota agora está entre 0 e 3.9, conceito E')
        else: print(f'Sua nota é {nota}')
    else: print(f'Sua nota {nota}')


def data():
    mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
           'Outubro', 'Novembro', 'Dezembro']
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mês: '))
    ano = int(input('Digite o ano: '))
    if 0 > mes > 12: print('Mẽs invalido!')
    else:
        print('Mês valido!')
        if 0 > dia > 31: print('Dia invalido!')
        elif mes == 2:
            if 0 < dia < 28: print('Dia valido!')
            elif dia == 29 and ano % 4 == 0 and ano % 100 != 0: print('Dia valido!')
            else: print('Dia invalido!')
        else: print('Dia valido!')





def main():
    data()


if __name__ == '__main__':
    main()
