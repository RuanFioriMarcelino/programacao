"""28) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
cada eleitor votar e ao final mostrar o número de votos de cada candidato. """
cand1 = 0
cand2 = 0
cand3 = 0
numero = int(input("Total de eleitores: "))
aux = 1
while aux <= numero:
    vot = int(input(f'Voto {aux}       \n'
                        '1 Para o candidato 1   \n'
                        '2 Para o candidato 2   \n'
                        '3 Para o candidato 3   \n'))
    if vot == 1:
        cand1 = cand1+1
    elif vot == 2:
        cand2 = cand2+1
    elif vot == 3:
        cand3 = cand3+1
    else:
        print("Votou nulo!!!")
    aux=aux+1

print(f"Votos para o candidato 1: {cand1}")
print(f"Votos para o candidato 2: {cand2}")
print(f"Votos para o candidato 3: {cand3}")