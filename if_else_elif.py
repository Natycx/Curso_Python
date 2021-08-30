"""
Estruturas condicionais
if(Se), else, elif (else if)

"""
idade = 26

"""
# Estrutura condicional if,else em C
if(idade < 18){
    printf("Menor de idade")
}else if(idade == 18){
    printf("Tem 18 anos")
}else {
    printf("Tem 18 anos")
}

"""

"""
# Estrutura condicional if, else em Java
if(idade < 18){
    System.out.println("Menor de idade")
}else if(idade == 18){
    System.out.println("Tem 18 anos")
}else {
    System.out.println("Tem 18 anos")
}
"""
if idade < 18:
    print("menor de idade")
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')