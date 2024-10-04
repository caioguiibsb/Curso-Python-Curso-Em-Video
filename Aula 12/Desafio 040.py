#Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final. de acordo com a media atingida media abaixo de 5 reprovado 5 a 6.9 recuperacao media 7 aprovado
nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
if (nota1+nota2)/2 < 5:
    print('Media a baixo de 5.0 REPROVADO!')
elif (nota1+nota2)/2 >= 5 and (nota1+nota2)/2 <= 6.9:
    print('Voçe esta na media RECUPERAÇÂO!')
else:
    print('Media de 7.0 ou superior APROVADO!')