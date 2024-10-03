#faça um programa que leia a largura ea altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintala sabendo que cada litro de tinta pinta uma area de 2m^2
altural=float(input('Digite a altural da parede: '))
largura=float(input('Digite a largura da parede: '))
area=altural*largura
print(f'A area da parede é {area}m^2')
print(f'Serão necessarios {area/2} litros de tinta para pintar')