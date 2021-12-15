"""
Len, Abs, Sum, Round

# Len

len() Retorna o tamanho (ou seja, o numero de itens de um iteravel)


# Só pra Revisar

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len({1, 2, 3, 4, 5, 6}))

print(len({'a': 1, 'b': 2}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len()

# Dunder

print('Geek University'.__len__())

# Abs
valor absoluto(modulo |x|)

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum soma
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], -5))
print(sum({1, 2, 3, 4, 5}))
print(sum((1, 2, 3, 4, 5)))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

# Round

round() - > Retorna um numero arredondado para n digito de precisão apos a casa decimal
Se a precisão não for informada retorna o inteiro mais proximo da entrada


"""
# Exemplos Round

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2, 2))



