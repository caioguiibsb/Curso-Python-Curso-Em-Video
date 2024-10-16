#Crie um programa que leia varios numeros inteiros pelo teclado. no final da excuçao, mostre a media entre todos os valores e qual foi o maior e o menor dos valores lidos. o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.
soma=0
s = 'S'
cont=0
maior=0
menor=0
while s == 'S':
    num = int(input('Digite um numero: '))
    s = str(input('Deseja digitar um novo numero? [S/N]')).upper()
    soma+=num
    cont+=1
    if cont == 1:
        maior=num
        menor=num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    media=soma/cont
print(f'contador {cont}A media dos valores é {media} o maior numero é {maior} e o menor é {menor}')