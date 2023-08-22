""" 9) Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
Euros. """

dolar = 4.98
euro =  5.43

nome = input("Digite seu nome: ")
dinheiro =float(input("Digite seu saldo em dinheiro R$ "))




print(f'Saldo convertido para o dólar: U${dinheiro/dolar}')
print(f'Saldo convertido para o euro: €{dinheiro/euro}')