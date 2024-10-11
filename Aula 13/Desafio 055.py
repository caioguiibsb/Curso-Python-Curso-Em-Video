#Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menos peso lidos
maior=0
menor=0
for c in range(1, 6):
    peso = float(input('Digite o peso: '))
    if c == 1:
        maior=peso
        menor=peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor=peso
print(f'O maior peso foi {maior} e o menor foi {menor}')