def numeros_lidos():
    n = int(input('Digite a quantidade de numeros: '))
    contador = 0
    maior = 0
    lista = []
    for i in range(n):
        valor = int(input('digite o valor: '))
        lista.append(valor)
        if maior > valor:
            contador += 1
        maior = valor

    print(max(lista))
    print(contador)


def pares():
    while True:
        valor = int(input('Digite um valor e 1000 para parar: '))
        if valor == 1000:
            break
        elif valor % 2 == 0:
            print(f'O numero {valor} é par!')
        else:
            print('Esse numero não é par!')


def numeros():
    n = int(input('Digite o numero: '))
    p = int(input('Digite o numero: '))
    par = 0
    impar = 0
    for i in range(n, p + 1):
        if i % 2 == 0:
            par += i
        else:
            impar += i
    print(f'Par = {par}')
    print(f'Impar: {impar}')


def notas():
    contador = 0
    media = 0
    while True:
        nota = int(input('Digite as notas entre 10 e 20: '))
        if 10 < nota > 20:
            break
        else:
            media += nota
            contador += 1
    print(f'A media é {media / contador}')


def divisor():
    n = int(input('Digite um numero: '))
    a = 1
    while a <= n:
        x = n % a
        a = a + 1
        if x == 0:
            print(a - 1)


def soma():
    soma = 0
    for i in range(1001):
        if i % 3 == 0 or i % 5 == 0:
            soma += i
    print(soma)


def harmonico():
    h = 1
    n = int(input('Digite um numero: '))
    for i in range(n + 1):
        if i >= 2:
            h += 1/i
    print(h)


def valor_e():
    h = 1
    fatorial = 1
    n = int(input('Digite um numero: '))
    for i in range(n + 1):
        if i >= 1:
            fatorial = fatorial * 1
            h += 1 /fatorial
    print(h)


def main():
    valor_e()


if __name__ == '__main__':
    main()