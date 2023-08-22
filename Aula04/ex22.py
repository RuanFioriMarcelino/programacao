""" 22) Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
Desconsiderando o valor 1000 da parada. """

lista = []
valor = 0

while valor != 1000:
    valor = int(input("Digite um valor inteiro: "))
    lista.append(valor)
print(len(lista))
print(sum(lista)-1000)

