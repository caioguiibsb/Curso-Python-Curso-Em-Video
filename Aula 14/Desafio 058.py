#escreva um programa que faça o computador pensar em um numero entre 0 e 5 e peça para o usuario tentar qual é o numero escolhido pelo computador. o programa devera dizer se o usuario venceu ou perdeu
import random
num = [1,2,3,4,5,6,7,8,9,10]
sort = random.choice(num)
cont=0
seunumb=0
while seunumb != sort:
    seunumb = int(input('Digite um numero: '))
    cont+=1
    if seunumb != sort:
        print(f'Você ERROU! tente novamente')
    else:
        print(f'Parabens voce acertou! foram nescessarias {cont} tentativas para acertar!')