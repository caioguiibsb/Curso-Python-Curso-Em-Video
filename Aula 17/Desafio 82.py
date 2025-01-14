listaMae=[]
listaImpar=[]
listaPar=[]
c=""
while True:
    if c in "Ss":
        valoradd = int(input(f'Digite o valor a ser inserido: '))
        listaMae.append(valoradd)
        c=str(input('Deseja continuar? S/N '))
    else:
        break
for numero in listaMae:
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
print("Lista de números pares:", listaPar)
print("Lista de números ímpares:", listaImpar)