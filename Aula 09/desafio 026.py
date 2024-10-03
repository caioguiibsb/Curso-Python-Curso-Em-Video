#faca um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A"; em que posicao ela aparece a primeira vez e posicao que aparece pela ultima vez.
frase = str(input("digite uma frase: ")).strip().upper()
print(f"A letra 'A' aparece {frase.count('A')} vezes na frase.")
print(f"A letra 'A' aparece pela primeira vez na posição {frase.find('A')}")
print(f"A letra 'A' aparece pela ultima vez na posição {frase.rfind}")
 