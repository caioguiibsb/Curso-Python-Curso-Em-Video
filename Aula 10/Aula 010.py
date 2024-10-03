nome = str(input('Qual é o seu nome? '))
if nome == 'caio':
    print('Que nome legal!')
print(f'Bom dia {nome}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A média das notas é {:.2f}'.format((n1 + n2)/2))
if (n1+n2/2) >= 6:
    print('Você está aprovado')
else:
    print('Você está reprovado')
