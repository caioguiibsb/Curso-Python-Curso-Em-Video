#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. para salarios superiores a R$1250 calcule um aumento de 10%; para os inferiosres ou iguais o aumento e de 15%
salario = float(input("Qual o salario do funcionario? R$"))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print(f"O salario do funcionario e de R${salario:.2f}")