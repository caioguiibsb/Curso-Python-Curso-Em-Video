#A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria. de acordo com a idade:
idade= int(input('digite sua idade: '))
if idade <= 9:
    print("Categoria MIRIM")
elif idade<=14:
    print("Categoria INFANTIL")
elif idade<=19:
    print("Categoria JUNIOR")
elif idade<=20:
    print("Categoria SENIOR")
elif idade>20:
    print("Categoria MASTER")