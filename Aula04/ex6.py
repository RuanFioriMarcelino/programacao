"""6) Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
comprar.

Considere: US$ 1.00 = R$ 5.41  """

dolar = 5.41
carteira = float(input("Digite o saldo em sua carteira R$ "))

print(f'Considerando a cotação do dólar dada você pode compra U$ {carteira/dolar}')