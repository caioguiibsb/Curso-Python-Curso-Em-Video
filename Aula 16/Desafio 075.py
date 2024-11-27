tup=()
pares=()
for c in range(0,4):
    num = int(input('Digite um numero: '))
    if num %2 == 0:
        pares+= (num,)
    tup += (num,) #Adicionando numero a tupla
print(tup)
print(f'O numero 9 apareceu {tup.count(9)} vezes')
if tup.count(3) <= 0:
    print('O valor 3 nao foi digitado em nenhuma posicao')
else:
    print(f'O numero 3 foi digitado na posicao {tup.index(3)+1}')
print(f'Os numeros pares foram: {pares}')