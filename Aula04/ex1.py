""" 1) Faça um script que leia dois números e retorne como resultado a soma deles. Faça um script que leia algo
pelo teclado e mostra na tela o seu tipo de dado.
 """

a = 12
b = 6
print(a+b)

c=input("Digite um valor: ")

print(f'É numério: {c.isnumeric()}')
print(f'É letra: {c.isalpha()}')
print(f'É só um espaço: {c.isspace()}')
print(f'É alpha numérico:{c.isalnum()}') 
print(f'Está em letras maiusculas: {c.isupper()}') 
print(f'Está em letras minusculas: {c.islower()}') 
print(f'Palavra capitalizada: {c.istitle()}') 