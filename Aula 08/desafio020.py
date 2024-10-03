#O mesmo professor do desafio anterior quer sortear a rodem de apresntacao de trabalhos dos alunos. faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
import random
nomes=['caio', 'guga', 'lucas', 'china']
random.shuffle(nomes)
print("A ordem será: ") 
print(nomes)