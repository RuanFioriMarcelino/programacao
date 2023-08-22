""" 17) Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 ∗ h) − 58
• Mulheres: (62, 1 ∗ h) − 44, 7 """

print("Digite 'm' para masculino e 'f' para feminino !!!")
resp =input(" ")
if resp == "m":
    h=float(input("Digite a sua altura: "))
    pesoideal = 72.7 * h - 58
    print(f'Peso ideal {pesoideal}')

if resp == "f":
    h=float(input("Digite a sua altura: "))
    pesoideal = 62.1 * h - 44.7
    print(f'Peso ideal {pesoideal}')

    
