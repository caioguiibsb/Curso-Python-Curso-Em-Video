#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'. Caso esteja errado, peça a digitacao novamente ate ter um valor correto.
sexo=''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        print(f"Voce digitou: {sexo}")
    else:
        print("Digite o valor Correspondente: [M/F]")
print('fim')
