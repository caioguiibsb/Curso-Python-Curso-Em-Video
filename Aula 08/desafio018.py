#faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno, e tangente desse angulo
import math
angulo=float(input("digite o valor do angulo: "))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print("o seno do angulo é {:.2f}".format(seno))
print("o cosseno do angulo é {:.2f}".format(cosseno))
print("a tangente do angulo é {:.2f}".format(tangente))
