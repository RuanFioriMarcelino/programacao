""" 8) Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m². """

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura*altura
quantidade_tinta = area/2

print(f'Área da parede = {area} metros')
print(f'Quantidade necessária de tinta para pintar a parede = {quantidade_tinta} litros')