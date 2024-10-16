#EScreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
num = int(input('Digite quantos numeros da sequencia de fibonacci deseja ver: '))
a=0
c=0
i=0
b=1
while i <= num:
    print(f'{c} → ')
    a=b
    b=c
    c=a+b
    i+=1
print('FIM')