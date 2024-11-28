#faca um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoees na lista. 
lista= []
for c in range(0,5):
    lista.append(int(input(f'digite um valor para a posicao {c}: ')))
valormax=max(lista)
valormin=min(lista)
posicoesmax= [i for i, v in enumerate(lista) if v == valormax]
posicoesmin= [i for i, v in enumerate(lista) if v == valormin]
print(f'valor maximo: {valormax} nas posicoes {posicoesmax}')
print(f'valor minimo: {valormin} nas posicoes {posicoesmin}')