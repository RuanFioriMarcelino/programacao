""" Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
a. Código da cidade; (digitado pelo usuário)
b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
Deseja-se saber:
b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
c. Qual a média de veículos nas cinco cidades juntas;
d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio """

maior = 0
menor = 99999999999999999999999

codigoLista = []
media = []
ind2 = []



for i in range(5):
    codigo      = int(input("Digite o codigo da cidade desejada: "))
    codigoLista.append(codigo)
    veiculos    = int(input("Digite a quantidade de veículos de passeio: "))
    acidentes   = int(input("Digite o número de acidentes:"))
    indice = veiculos/acidentes
    ind2.append(indice)

    if indice < menor:
        menor = indice
        menorcidade = codigo

    if indice > maior:
        maior = indice
        maiorcidade = codigo

    if veiculos < 2000:
        media.append(acidentes)
        
mediaI= sum(ind2)/len(ind2)
print(f'Maior índice de acidentes na cidade de {maiorcidade}, índice de {maior} ')
print(f'Menor índice de acidentes na cidade de {menorcidade}, índice de {menor} ')
print(f'Média de índices de todas cidades é de {mediaI}')

if len(media)>0:
    menor2000=sum(media) / len(media)
    print(f'Média de acidentes com menos de 2000 veículos é de {menor2000}')