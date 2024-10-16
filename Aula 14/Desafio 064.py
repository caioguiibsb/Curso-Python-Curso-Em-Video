#Crie um programa que leia varios numeros interos pelo teclado. O programa so vai parar quando o usuario digitar o valor 999,  que é a condiçao de parada. no final mostre quantos numeros foram digitadso e qual foi a soma entre eles.
i=0
soma=0
qtd=0
while i != 999:
    num=int(input('Digite um numero: '))
    if num == 999:
        i=999
    else:
        soma+=num
        i+=1
        qtd=i
print(f"A Soma entre os numeros foram {soma}")
print(f'Foram Digitados {qtd} numeros')