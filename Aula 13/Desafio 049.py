#Refaça  o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando o laco for.
n = int(input('Voçê deseja ver a tabuada de qual numero?: '))
b = int(input(f'até que numero voce deseja que {n} seja multiplicado?: '))
for c in range(0, b+1):
    print(f'{n} x {c} = {n*c}')