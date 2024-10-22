#Crie um programa que leia verios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar 999, que é a condiçao de parada. no final mostre quantos numeros foram digitados e qual foi a soma entre eles.
n= c= s=0
while True:
    n=int(input('Digite um numero: [Digite 999 para parar]'))
    if n == 999:
        break
    c+=1
    s=s+n
print(f'Foram digitados {c} numeros e a soma dos valores é: {s}')