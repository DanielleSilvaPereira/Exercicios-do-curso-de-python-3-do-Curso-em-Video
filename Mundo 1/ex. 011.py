# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = int(input('Digite a altura da parede: '))
largura = int(input('Digite a largura da parede: '))
print('A area da parede é {}, sendo nescessário {}m^2 de tinta para pintar ela inteira.'.format(altura*largura, (altura*largura)/2))