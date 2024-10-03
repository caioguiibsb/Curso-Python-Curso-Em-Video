#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
salario = float(input("Digite o salario do funcionario: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f"O novo salario do funcionario é: {novo_salario:.2f}")