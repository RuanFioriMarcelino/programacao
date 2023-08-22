""" 21) Crie um programa que leia dois valores e mostre na tela um menu :
a. Somar
b. Multiplicar
c. Maior
d. Menor
e. Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso """
maior = 0
menor = 999999999
op = "f"

nmr1=int(input("Digite o primeiro valor: "))
nmr2=int(input("Digite o segundo valor: "))

if nmr1 > maior:
    maior = nmr1

if nmr2 > maior:
    maior = nmr2

if nmr1 < menor:
    menor = nmr1

if nmr2 < menor:
    menor = nmr2

while op != 'e':
    op = input('Escolha uma operação para ser realizada abaixo: \n'
                'a. Somar \n'
                'b. Multiplicar \n'
                'c. Maior \n'
                'd. Menor \n' 
                'e. Sair do programa \n'
                ' ')

    if op == 'a':
        soma = (nmr1+nmr2)
        print(f'A soma dos números são: {soma}')
    if op == 'b':
        multplicacao = (nmr1*nmr2)
        print(f'A multiplicação entre os números são: {multplicacao}')
    if op == 'c':
        print(f'Maior número: {maior}')
    if op == 'd':
        print(f'Menor número: {menor}')