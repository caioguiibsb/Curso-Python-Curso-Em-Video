#Faça um programa que leia um numero inteiro e diga se ele é ou nao um primo.
num = int(input('Digite um numero: '))
if num % 2 != 0:
    print(f"O numero {num} é um primo")
else: print("Nao é um numero primo!")