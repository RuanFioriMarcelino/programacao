nota1 = float(input("Digite a nota da prova 1 valendo peso 5: "))
nota2 = float(input("Digite a nota da prova 2 valendo peso 5: "))
nota3 = float(input("Digite a nota da prova 3 valendo peso 10: "))

media = (nota1+nota2+nota3)/2

if media >= 6:
    print(f'Aluno aprovado com {media} pontos.')
if media < 6:
    print(f'Aluno reprovado com {media} pontos')