#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "santo".
nome_cidade = input("Digite o nome da cidade: ")
if nome_cidade.lower().startswith("santo"):
    print('Sim o nome da cidade começa com santo')
else:print('Não o nome da cidade não começa com santo')

