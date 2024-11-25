lanche = ('Hamburguer', 'suco', 'pizza', 'Pudim')

for comida in lanche:       #se nao precisar da posicao do item
    print(f'Eu vou comer {comida}')

#se precisar da posicao do alimento
for cont in range(0, len(lanche)): #aq voce pode pegar a posicao pelo cont
    print(f"Eu vou comer {lanche[cont]} na posica {cont}")

for comida in lanche: #aq voce apenas pode mostrar o item da posicao
    print(f"Eu vou comer {comida}")

# outro metodo usando o enumerate
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicao {pos}")

print(f"Comi pra caramba")

