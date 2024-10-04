#Escreva um programa que leia dois numeros inteiros e compareos mostrando na tela uma mensagem- o primeiro é maior o segundo é maior- nao exite valor maior os dois sao iguais.
num1 = int(input('Digite o primeiro um numero'))
num2 = int(input('Digite o segundo um numero'))
if num1 > num2:
    print(f'O primeiro numero {num1} é maior que {num2}')
elif num1 < num2:
    print(f'O segundo numero {num2} é maior que {num1}')
else:
    print('Os dois valores sao iguais')
