#Crie um programa que faca o computador jogue jokenpo com voce
import random
jogador = int(input(" Escolha\n [0] - pedra\n [1] - papel\n [2] - tesoura\n"))
opcoes = ['pedra', 'papel', 'tesoura']
computador = random.randint(0,2)
print("-="*20)
print(f'Voce jogou {opcoes[jogador]}')
print(f'O computador jogou {opcoes[computador]}')
print("-="*20)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Voce perdeu!')
    elif jogador == 2:
        print('Voce ganhou!')
    else:
        print('Jogada Invalida')
if computador == 1:
    if jogador == 0:
        print('Voce ganhou!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Voce perdeu!')
    else:
        print('Jogada Invalida')
if computador == 2:
    if jogador == 0:
        print('Voce ganhou!')
    elif jogador == 1:
        print('Voce perdeu!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Invalida')