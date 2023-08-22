""" O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de
conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá
receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser
informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e
perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta
operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser
conforme o exemplo abaixo:
    a. Lojas Tabajara
    b. Produto 1: R$ 2.20
    c. Produto 2: R$ 5.80
    d. Produto 3: R$ 0
    e. Total: R$ 9.00
    f. Dinheiro: R$ 20.00
    g. Troco: R$ 11.00
    h. ...  """


nmr = 1

cai = []


while nmr != 0:
    nmr = float(input("Digite o valor, '0 para sair' : "))
    cai.append(nmr)

tota = sum(cai)

dinheiro = float(input("Digite a quantia dada pelo cliente: "))
troco = dinheiro - tota
if dinheiro >= tota:
    print(f'Troco a dar pro cliente {troco}')
else:
    print(f'Quantia faltante {troco * - 1}')