#escreva um programa que faça o computador pensar em um numero entre 0 e 5 e peça para o usuario tentar qual é o numero escolhido pelo computador. o programa devera dizer se o usuario venceu ou perdeu
import random
num = [1,2,3,4,5]
sort = random.choice(num)
seunumb = int(input('Digite um numero: '))
if seunumb == sort:
    print('Parabéns você ganhou')
else:
    print(f'Você perdeu, o numero sorteado foi {sort}')