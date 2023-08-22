""" 19) Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
a. Soma de 2 numeros.
b. Diferença entre 2 números (maior pelo menor).
c.Produto entre 2 números.
d. Divisão entre 2 números (o denominador não pode ser zero). """

nmr1=int(input("Digite o primeiro valor: "))
nmr2=int(input("Digite o segundo valor: "))

op = input('Escolha uma operação para ser realizada abaixo: \n'
            'a - Soma de 2 numeros.\n'
            'b - Diferença entre 2 números (maior pelo menor).\n'
            'c - Produto entre 2 números.\n'
            'd - Divisão entre 2 números (o denominador não pode ser zero).\n'
            ' ')
if op == 'a':
    soma = (nmr1+nmr2)
    print(f'A soma dos números são: {soma}')
if op == 'b':
    menos = (nmr1-nmr2)
    print(f'A diferença entre os números são: {menos}')
