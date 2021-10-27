def multiplos_de_3():
    multiplos = []
    novo = []
    for i in range(100):
        if i % 3 == 0:
            multiplos.append(i)

    for i in range(5):
        novo.append(multiplos[i])

    print(novo)


def de_1_a_100():
    for i in range(100):
        print(i)
    contador = 0
    while True:
        print(contador)
        if contador == 100:
            break
        contador += 1
    while contador >= 0:
        print(contador)
        contador -= 1


def contagem_regressiva():
    contagem = 10
    while True:
        print(contagem)
        if contagem == 1:
            print('FIM!')
            break
        contagem -= 1


def de_mil_em_mil():
    n = int(input('Digite um numero acima de mil: '))
    for i in range(0, n, 1000):
        print(i)
        if i == 10000:
            break


def soma():
    contador = 0
    soma = 0
    while contador < 10:
        n = int(input('Digite um numero: '))
        contador += 1
        soma += n
    print(soma)


def media():
    contador = 0
    soma = 0
    while contador < 10:
        n = int(input('Digite um numero: '))
        contador += 1
        soma += n
    print(f'A media foi {soma / contador}')


def media_ignorando_numeros_inteiros():
    contador = 0
    soma = 0
    while contador < 10:
        n = int(input('Digite um numero: '))
        if n >= 0:
            contador += 1
            soma += n
        else:
            contador += 1

    print(f'A media foi {soma / contador}')


def max_min_valor():
    lista = []
    while True:
        n = int(input('Digite um numero: '))
        if n == 0:
            break
        else:
            lista.append(n)
    print(f'Valor minimo: {min(lista)} Valor maximo: {max(lista)}')


def numeros_naturais_impares():
    n = int(input('Digite um numero: '))
    lista = []
    for i in range(n):
        if i == 0 or i == 1:
            lista.append(i)
        elif i % 3 == 0 and i % 2 != 0:
            lista.append(i)
    print(lista)


def soma_numeros_pares():
    lista = [x for x in range(0, 100, 2)]
    soma = 0
    for x in range(len(lista)):
        soma += lista[x]
    print(soma)


def numeros_naturais():
    n = int(input('Digite o numero: '))
    for i in range(n + 1):
        print(i)


def numeros_naturais_decrescente():
    n = int(input('Digite o numero: '))
    numeros = []
    for i in range(n + 1):
        numeros.append(i)
    print(numeros[::-1])


def numeros_pares():
    while True:
        n = int(input('Digite um numero: '))
        if n % 2 == 0:
            break
    for i in range(n + 1):
        if i % 2 == 0:
            print(i)


def numeros_impares():
    while True:
        n = int(input('Digite um numero: '))
        if n % 3 == 0:
            break
    for i in range(n + 1):
        if i == 1:
            print(i)
        elif i % 3 == 0:
            print(i)


def soma_primeiros():
    n = int(input('Digite um numero posito: '))
    soma = 0
    for i in range(n + 1):
        soma += i
    print(soma)


def main():
    soma_primeiros()


if __name__ == '__main__':
    main()