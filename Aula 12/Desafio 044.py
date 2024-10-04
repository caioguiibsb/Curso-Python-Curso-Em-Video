#Elabore um programa que calcule o valor a ser pago por um produto. considerando o preco normal e condicao de pagamento avista 10% desconto avista cartao 5% desconto ate duas vezes cartao preco normal 3x ou mais no cartao juros 20%juros
valorproduto=float(input("Digite o valor do produto: "))
metodopagemento= int(input(' Digite o Numero da Opcao desejada\n 1 - 10% Desconto Dinheiro \n 2 - 5% desconto Cartao Avista \n 3 - Duas vezes no cartao sem juros \n 4- 3x ou mais com 20% juros \n'))
if metodopagemento == 1:
    valorproduto = valorproduto-(valorproduto*0.10)
    print(f"O vaor a ser pago é {valorproduto}")
elif metodopagemento ==2:
    valorproduto = valorproduto-(valorproduto*0.05)
    print(f"O vaor a ser pago é {valorproduto}")
elif metodopagemento == 3:
    print(f'Valor a pagar {valorproduto}')
elif metodopagemento == 4:
    valorproduto = valorproduto+(valorproduto*0.20)
    print(f"O vaor a ser pago é {valorproduto}")
else:
    print('Opcao invalida.')