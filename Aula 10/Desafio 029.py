#Escreva um programa que leia a velocidade de um carro. se ele ultrapasssar 80km. mostre uma mensagem dizendo que foi multado; a multa vai custar 7R$ por cada km acima do limite

vel=float(input('Digite a velocidade do veiculo: '))
if vel>80:
    multa= (vel-80)*7
    print(f'Você foi multado, a multa é de R${multa}')
else: print("Voce nao foi multado!")