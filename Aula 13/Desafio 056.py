#Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. no final do programa, mostre: a media de idade, qual é o nome do homem mais velho. quantas mulheres tem menos de 21 anos
somaidades=0
maioridadehomem=0
nomevelho = ''
qtdmulher = 0
for c in range(1, 5):
    print(f'----- {c}º Pessoa -----')
    nome = str(input("Nome: ")).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidades+=idade
    if c == 1 and sexo in 'Mm':
        nomevelho = nome
        maioridadehomem = idade
    if sexo in 'Mn' and idade > maioridadehomem:
        nomevelho=nome
        maioridadehomem = idade
    if sexo in 'Ff' and idade < 20:
        qtdmulher+=1
print(f"A media de idade do grupo é: {somaidades/4}")
print(f"O homem mais velho tem {maioridadehomem} e se chama {nomevelho}")
print(f'Ao todo sao {qtdmulher} mulheres com menos de 20 anos')