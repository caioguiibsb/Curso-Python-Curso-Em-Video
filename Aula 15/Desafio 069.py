print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
idade = 0
sexo=''
qtdhomem=0
qtdmulher=0
idadeall=0
while True:
    idade= int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    if idade >= 18:
        idadeall += 1
    if sexo == 'M':
        qtdhomem += 1
    if sexo == 'F' and idade < 20:
        qtdmulher += 1
    cont= str(input('Quer continuar? [S/N] ')).upper()
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos : {idadeall}')
print(f'Ao todo temos {qtdhomem} homens cadastrados')
print(f'E temos {qtdmulher} mulheres com menos de 20 anos')
