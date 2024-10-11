#faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500.
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(f"O Numero {c} é multiplo de 3")
        soma+=c
print(f'A soma de todos os primos sao: {soma}')