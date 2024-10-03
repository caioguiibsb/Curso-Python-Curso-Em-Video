#escreva um programa que pergunte a quantidade de km pecorrido por um carro alugado e a quantidade de dias pelo quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
km=float(input('Digite quantos KM foram pecorridos com o carro: '))
dias=float(input('Digite quantos dias ficou com o carro: '))
preco=60*dias+0.15*km
print(f'O valor a ser pago é {preco}')