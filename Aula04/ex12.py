""" Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
os itens repetidos """
lista = ['a', 'b', 'a', 'c', 'c']
l = []


for i in lista:
    if i not in l:
        l.append(i)
    else:
        l.append(i)
        print(i)