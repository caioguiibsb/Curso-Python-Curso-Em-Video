print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
import random
v=0
while True:
    vcnum = int(input('Diga um valor: '))
    botnum= random.randint(0,10)
    total = vcnum+botnum
    tipo=' '
    while tipo not in'PI':
        tipo= str(input('Par ou impar?[P/I]')).upper()[0]
    print(f"Voce jogou {vcnum} e o o bot jogou {botnum}. Total de {total}", end='')
    print(' DEU PAR' if total%2 == 0 else ' DEU IMPAR')

    if tipo == 'P':
        if total%2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total%2==1:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu')
            break
print(f'Vamos jogar novamente! Voce ganhou {v} vezes')