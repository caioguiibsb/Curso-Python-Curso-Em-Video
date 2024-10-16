#Faça um progrma que leia um numero qualquer e mostre o seu fatorial.
num=int(input('Digite um numero para obter o seu fatorial:'))
cont=1
fatorial=1
while cont <= num:
    fatorial*=cont
    cont+=1
print(f'O fatorial de {num} é: {fatorial}')

