"""25) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

senha   = " "
nome    = " "
while senha == nome:
    nome = input("Digite seu nome de usuário: ")
    senha = input('Digite uma senha diferente de seu nome: ')
    if  senha == nome:
        print('Sua senha não pode ser igual o nome de usuário')
    