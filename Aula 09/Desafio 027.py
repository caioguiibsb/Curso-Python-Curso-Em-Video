#Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente. 
#Ex: Ana Silva
#Primeiro nome: Ana
#Ultimo nome: Silva
nome = input("Digite o seu nome completo: ")
nome = nome.split()
print(f"Primeiro nome: {nome[0]}")
print(f"Ultimo nome: {nome[-1]}")