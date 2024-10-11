#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas dos que forem pares. se o valor for impar desconsidere-o
soma=0
for c in range(1, 6+1):
    num = int(input(f'Ditege o {c}º numero: ')) 
    if num % 2 ==0:
        soma+=num
print(f'A soma dos valores foram: {soma}')
