for c in range(0, 10, 2):
    print(f"Loop {c} is running")
print("fim")

i=int(input('Inicio: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print("fim")

s=0
for c in range(0, 4):
    n=int(input('Digite um valor: '))
    s = s + n
print('O somatório dos valores é {}'.format(s))