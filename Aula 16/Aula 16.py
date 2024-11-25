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

a = (2, 5 ,4)
b = (5, 8, 1, 2)
c = b + a
print(len(c)) #quantidade de elemntos na tupla

a = (2, 5 ,4)
b = (5, 8, 1, 2)
c = b + a
print(len(c.count(5))) #quantas vzs aparece o numero 5 na tupla

a = (2, 5 ,4)
b = (5, 8, 1, 2)
c = b + a
print(len(c.index(8))) #mostra em qual posicao esta o numero 8 (COMEÇANDO DO ZERO)
print(len(c.index(2, 5))) #mostra em qual posicao esta o numero 2 apatir da 5 posicao

pessoa = ("gustvo", 39, 'M', 99.88)
del(pessoa) #apaga tupla por completo
print(pessoa)
