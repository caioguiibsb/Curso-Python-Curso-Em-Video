#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa devera ler um numero pelo taclado(entre 0 e 20) e mostralo por extenso.
num=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    seunum=int(input('Digite um numero entre 0 e 20: '))
    if seunum >= 0 and seunum <= 20:
        print(f'Voçe digitou o numero {num[seunum]}')
        break
    else:
        print('Tente novamente')