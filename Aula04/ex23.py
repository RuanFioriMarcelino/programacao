""" 23) Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a escrever valores. """
 
lista = []
maior = 0
menor = 99999999999999999
op = "z"
cont = 0

while op == 's':
    nmr = int(input('Digite um valor: '))
    cont+=1
    op = input("Deseja continuar, 's' para sim 'n' para não. ")
    lista.append(nmr)

    if nmr > maior:
        maior = nmr

    if nmr < menor:
        menor = nmr

soma = sum(lista)
media = lista

print(f'Média dos valores {media}')
print(f'O maior número entre eles {maior}')
print(f'O menor número entre eles {menor}')
print(f'A média dos número {media}')

