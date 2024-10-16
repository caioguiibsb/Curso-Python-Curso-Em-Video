#Desenvolva um programa que leia o primero termo e a razao de uma PA. no final mostre os 10 primeiros termos dessa progressao. usando While
termo = int(input('Digite o primeiro termo: '))
rasao = int(input('Digite razao: '))
cont=0
while cont < 10:
    print(f"Os Termosa sao: {termo}")
    termo +=rasao
    cont+=1