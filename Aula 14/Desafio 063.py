#EScreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
num = int(input('Digite quantos numeros da sequencia de fibonacci deseja ver: '))
i=0
soma=0
while i <= num:
    soma = i + (i+1)
    print(soma)
    i+=1