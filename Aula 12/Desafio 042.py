#refaca o desafio 35 acrescentando se o triangulo sera formado por equilatero isosceles, escaleno.
print('Analisador de Triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os segmentos podem formar um triângulo')
    if r1 == r2 ==r3:
        print("Triangulo Equilatero. ")
    elif r1 != r2 != r3:
        print("Triangulo escaleno")
    else:
        print('Triangulo isosceles')
else:
    print('Os segmentos não podem formar um triângulo')