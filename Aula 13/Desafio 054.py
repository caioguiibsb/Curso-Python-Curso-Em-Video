#crie um progreama que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
somaidades=0
for c in range(1, 7+1):
    anonasc = int(input(f'Digite a data de nascimento do {c}º: '))
    if 2024 - anonasc >= 21:
        somaidades=somaidades+1
print(f"Somente {somaidades} dos anos informados sao maiores de idades!")
print(f"Somente {7-somaidades} dos anos informados sao menores de idades!")