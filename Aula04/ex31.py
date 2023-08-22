""" 31) Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo. """

import random

op = input('par ou impar? ')
numero = int(input('escolha um numero: '))
comp=random.randint(0, 10)
total = numero + comp
r = total%2

if op == 'par':
    if r == 0:
        print(f'Computador jogou {comp} total deu {total} e você ganhou !')
    else:
        print(f'Computador jogou {comp} total deu {total} e você perdeu !!!')
       
elif op == 'impar':
    if r == 1:
        print(f'Computador jogou {comp} total deu {total} e você ganhou !')
    else:
        print(f'Computador jogou {comp} total deu {total} e você perdeu !!!')
