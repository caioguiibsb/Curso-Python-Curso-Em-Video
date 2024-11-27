itens=('lapis', 1.50, 'caneta', 2.00, 'caderno', 30.00, 'borracha', 2.00)

for c in range(0, len(itens)):
        if c% 2 ==0:
                print(f'{itens[c]:.<30} R$ {itens[c+1]:>5.2f}')
