num=[2, 5, 9, 1,2]
num[3] = 4
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop(1)
print(num)
if 2 in num:
    print(num.remove(2))
else:
    print('Nao achei o numero')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

'''for v in valores:
    print(f"{v}...", end="")'''
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f"\nNa posição {c} encontrei o valor {v}", end="")

