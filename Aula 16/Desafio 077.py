#crie um programa que tenha uma tupla com varias palavras depois disso voce deve mostrar, para cada palavra quais sao as suas vogais.
tupla=("casa", "teto", "cerveja")
vogais=('a', 'e', 'i', 'o', 'u')
for palavra in tupla:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
