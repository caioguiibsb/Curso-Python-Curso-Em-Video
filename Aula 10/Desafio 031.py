#Desenvolva um programa que pergunte a distancia de uma viagem em km. calcule o preco da passagem, cobrando R$0,50 por km para viagem da ate 200km e R$0,45 para viajens mais longas
distancia = float(input("Digite o valor da viajem em km: "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O valor da passagem é R${preco:.2f}")