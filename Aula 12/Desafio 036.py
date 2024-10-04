#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. o programa vai perguntar o valor da casa, salario do comprador e em quantos anos ele vai pagar. calcule o valor da prestacao mensal, sabendo que ela nao pode exeder 30% do salario ou entao o emprestimo sera negado

valorcasa= float(input("Digite o valor do imovel: "))
salario= float(input("Digite o valor do seu salario: "))
anos= int(input("Em quantos anos voce vai pagar: "))
salario =salario*0.30
prestacao= valorcasa / (anos*12)
if prestacao > salario:
    print('Emprestimo negado. Seu salario nao é suficiente.')
else:
    print(f'Emprestimo aprovado. prestacaoR${prestacao}')
