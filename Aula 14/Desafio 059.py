#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] soma
#[2]multiplicar
#[3]maior
#[4]novos numeros
#[5]Sair do programa
#Seu programa devera realizar a operacao em cada caso

num1 = float(input("Digite Um Valor:"))
num2 = float(input("Digite o Segundo Valor:"))
opcao=0
while opcao != 5:
    print('Digite a opção Desejada:')
    opcao= int(input('[1] soma\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]Sair do programa:\n'))
    if opcao == 1:
        print(f'A soma dos valores de {num1}+{num2} é: {num1+num2}')
    if opcao == 2:
        print(f'A Multiplicacao dos valores de {num1} * {num2} é: {num1*num2}')
    if opcao == 3:
        if num1 == num2:
            print(f"O numero {num1} é igual {num2}")
        elif num1 > num2:
            print(f"O numero {num1} é maior que {num2}")
        else:
            print(f"O numero {num2} é maior que {num1}")
    if opcao == 4:
        num1 = float(input("Digite novemente Um primero Valor:"))
        num2 = float(input("Digite novamente UM Segundo Valor:"))
print('Voce saiu do Programa!')