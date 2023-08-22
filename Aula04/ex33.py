"""33) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são: 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero. """

cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0 
cand5 = 0
cand6 = 0

voto2 = []
voto1 =1
while voto1 != 0:
    voto1 = int(input('1 Para Ricardão      \n'
                     '2 Para Sid Moreira    \n'
                     '3 Para Fred           \n'
                     '4 Para Joninhas       \n'
                     '5 Para Nulo           \n'
                     '6 Para Branco         \n'
                     '0 Para sair           \n'))
    voto2.append(voto1)

for i in voto2: 
    if i == 1: 
        cand1 = cand1 + 1
    if i == 2:
        cand2 = cand2 + 1
    if i == 3: 
        cand3 = cand3 + 1
    if i == 4:
        cand4 = cand4 + 1
    if i == 5:
        cand5 = cand5 + 1
    if i == 6: 
        cand6 = cand6 + 1

tot = len(voto2)-1
totalnulo =   cand5/tot * 100
totalbranco = cand6/tot * 100

print(f'Total de votos para Ricardão: {cand1}')
print(f'Total de votos para Sid Moreira: {cand2}')
print(f'Total de votos para Fred: {cand3}')
print(f'Total de votos para Joninhas: {cand4}')
print(f'total de votos em nulos: {cand5}')
print(f'total de votos em Branco: {cand6}')
print(f'Porcentagem de votos nulos: {totalnulo}')
print(f'Porcentagem de votos em branco: {totalbranco}')