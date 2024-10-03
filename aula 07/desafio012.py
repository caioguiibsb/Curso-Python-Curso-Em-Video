#faça um algoritimo que leia o preço de um produto e mostre seu novo preco, com 5% de desconto.
preco=float(input('Digite o preço do item:'))
valorfinal=preco-(preco*0.05)
print(f'O Desconto sera de {preco*0.05:.3} e o valor final do produto ficara em {valorfinal}')