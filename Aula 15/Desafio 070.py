nomeproduto=''
valorproduto=0
valortotal=0
maisbarato=0
maiscaro=0
continuar=''
cont=0
nomebarato = ''
while True:
    cont+=1
    nomeproduto = str(input('Digite o nome do produto: '))
    valorproduto= float(input("Digite o valor do produto: "))
    valortotal+=valorproduto
    if cont == 1:
        maisbarato = valorproduto
        nomebarato = nomeproduto
    if valorproduto < maisbarato:
        maisbarato = valorproduto
        nomebarato = nomeproduto
    if valorproduto > 1000:
        maiscaro+=1
    continuar = str(input('Quer continuar? [S/N]')).upper()[0]
    if continuar == 'N':
        break

print(f'O total da compra foi R${valortotal}')
print(f'Temos {maiscaro} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${maisbarato}')
