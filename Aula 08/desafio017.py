#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
CatOP=float(input("Digite o valor do cateto oposto: "))
CatAD=float(input("Digite o valor do cateto adjacente: "))
hipot= math.hypot(CatOP, CatAD)
print("O comprimento da hipotenusa é: ", hipot)