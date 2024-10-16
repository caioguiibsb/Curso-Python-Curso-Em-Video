#Desenvolva um programa que leia o primero termo e a razao de uma PA. no final mostre os 10 primeiros termos dessa progressao. usando While
termo = int(input('Digite o primeiro termo: '))
rasao = int(input('Digite razao: '))
cont=0
qtd=10
while cont < qtd:
    print(f"Os Termosa sao: {termo}")
    termo +=rasao
    cont+=1
s=str(input('Deseja adicionar mais valores?[S/N]')).upper()
if s == 'S':
    numS=int(input('Digite mais quantos termos deseja ver: '))
    qtd+=numS
    while cont < qtd:
        print(f"Os Termosa sao: {termo}")
        termo +=rasao
        cont+=1