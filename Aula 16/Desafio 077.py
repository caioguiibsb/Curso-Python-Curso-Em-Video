#crie um programa que tenha uma tupla com varias palavras depois disso voce deve mostrar, para cada palavra quais sao as suas vogais.
tupla=("casa", "teto", "cerveja")
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
 