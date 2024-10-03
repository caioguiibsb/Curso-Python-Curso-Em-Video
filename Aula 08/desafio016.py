#crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porçao inteira.
import math
num=float(input('Digite um numero: '))
print(f"O numero na sua porçao inteira é: {math.trunc(num)}")