"""
Escopo de variáveis

/                    /

Dois casos de escopo:

1 -> variaveis globais: são reconhecidas, ou seja, seu escoco compreende
todo o programa

2 -> Variaveis locais são reconhecidas apenas no bloco aonde foi declarada
ou seja, seu escopo está limitado ao bloco onde foi declarada.

para declarar variavel em python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que
ao declararmos uma variavel, nos não colocamos o tipo de dado dela.
este tipo é inferido ao atribuirmos o valor a mesma

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

"""

numero = 42  # Exemplo de varivel global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 'oi'
print(nao_existo)

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10  # A variave 'novo' está declarada localmente dentro do bloco do if. Portando é local
    print(novo)

print(novo)