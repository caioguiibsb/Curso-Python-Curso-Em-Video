#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de numeros gerados e tambem indique o menor eo maior valor que estao na tupla.
import random
tupla=()
maior=0
menor=0
for c in range(0,5):
    rand = random.randint(0,9)
    tupla += (rand,)
    if c == 0:
        maior=rand
        menor=rand
    if maior < rand:
        maior = rand
    if rand < menor:
        menor = rand
print(f'Os valore sorteados foram: {tupla}')
print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')