""" Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre
ele. """

c = input('Digite algo: ')
print(f'É numério: {c.isnumeric()}')
print(f'É letra: {c.isalpha()}')
print(f'É só um espaço: {c.isspace()}')
print(f'É alpha numérico:{c.isalnum()}') 
print(f'Está em letras maiusculas: {c.isupper()}') 
print(f'Está em letras minusculas: {c.islower()}') 
print(f'Palavra capitalizada: {c.istitle()}') 