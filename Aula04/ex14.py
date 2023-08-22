#14) Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista

lista = ["a","b","c","d","e"]

elemento = input("Digite o elemento que deseja buscar na lista: ")
print(f'Verificando se {elemento} está na lista:')

if elemento in lista:
    print("Elemento na lista!!! ")
    print(f'Posição {lista.index(elemento)}')
else:
    print("Elemento não está na lista!!!")