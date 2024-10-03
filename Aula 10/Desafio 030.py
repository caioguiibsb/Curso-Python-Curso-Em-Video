#Crie um programa que leia um numero qualquer e mostre se ele e par ou impar
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))