#Desenvolva uma logica que leia o peso e altura de uma pessoa calcule seu imc e mostre o status de acordo com a tabela abaixo. abaixo peso 18.5, entre 18.5 e 25 peso ideal. 30 a 40 obeso. acima  obesidade morbida;
altura= float(input("Digite sua altura: "))
peso= float(input("Digite seu Peso: "))
imc=peso/(altura*2)
if imc < 18.5:
    print("Abaixo do peso")
elif imc>=18.5 and imc <= 25:
    print("Peso ideal")
elif imc>25 and imc <= 30:
    print("Peso sobrepeso")
elif imc>30 and imc <= 40:
    print("Peso obesidade")
else:
    print("Obesidade morbida")