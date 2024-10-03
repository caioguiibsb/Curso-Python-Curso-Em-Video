#crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.

nome = input("Digite o nome da pessoa: ")
if "silva" in nome.lower():
    print('Sim o nome tem silva')
else:print("Nao tem o nome silva")

print(f'Seu nome tem silva? {'silva' in nome.lower()}')