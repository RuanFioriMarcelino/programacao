""" 7) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
de aumento. """

produto = float(input("Digite o valor do produto R$ "))


print(f'Valor do produto com 5% de desconto R${produto-produto*0.05}')
print(f'Valor do produto com 10% de aumento R${produto+produto*0.10}')