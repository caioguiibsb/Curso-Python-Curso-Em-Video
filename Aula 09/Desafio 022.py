#crie um programa que leia o nome completo de ma pessoa e mostre; O nome com todas as letras maiusculas; O nome com todas minusculas; quantas letras ao todo sem considerar espacos; quantas letras tem o primeiro nome
nome= str(input('Digite seu nome completo: '))
print(f'seu nome com todas as letras maiusculas fica: {nome.upper()}')
print(f'seu nome com todas as letras minuscula fica: {nome.lower()}')
print(f'seu nome tem {len(nome.replace(" ",""))} letras')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')
