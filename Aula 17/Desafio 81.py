lista=[]
c=''
cont=0
cinco=0
while True:
    if  c in 'Ss':
        n = int(input('Digite o valor a ser inserido: '))
        lista.append(n)
        cont+=1
        if n ==5:
            cinco+=1
        c= str(input('Deseja continuar? S/N '))
    else:
        break
lista.sort(reverse=True)
print(f'Foram digitados {cont} numeros')
print(f'A lista digitada em ordem decresente foi foi {lista}')
print(f'O valor 5 foi digitado {cinco} vezes')