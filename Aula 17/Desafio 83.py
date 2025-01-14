c = str(input('Digite a expressão matematica: '))
qtd = c.count('(')
qtd1 = c.count(')')
if qtd == qtd1:
    print('A Expressao é valida!')
else:
     print('A Expressao NãO é valida!')