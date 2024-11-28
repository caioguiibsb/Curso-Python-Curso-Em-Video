#crie um program onde o usuario possa digitar varios valores numericos e cadastre-os em uma listas. caso o numero ja exista la dentros, ele nao sera adicionado. No final, serao exibidos todos os valores unicos digitados em ordem crescente.
c=''
lista=[]
valoradd=0
while True:
    if c in 'sS':
        valoradd = int(input(f'Digite o valor a ser inserido: '))
        if valoradd in lista:
            print('Valor duplicado! nao vou adicionar.')
        else:
            lista.append(valoradd)
            print(f'valor adicionado com sucesso!')
        c=str(input('Deseja continuar? S/N '))
    else:
        break
lista.sort()
print(f'Voce digitou os valores {lista}')