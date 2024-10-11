#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando espacos.
palavra=str(input("Digite uma palavra: ")).lower().strip().replace(' ','')
if palavra == palavra[::-1]: 
    print('É palindromo')
else: print('Nao e palindromo')

#Esse desafio foi massa!