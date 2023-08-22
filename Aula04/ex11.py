""" 11) Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
ao final mostrar seu nome e salário final calculado."""

nome = input("Digite seu nome: ")
nmrhoras = float(input("Digite o número de horas trabalhadas: "))
vlrhora = float(input("Digite o valor da hora trabalhada R$ "))

salariobruto = nmrhoras*vlrhora
salariofinal = salariobruto - salariobruto*0.02

print(f'Salário bruto de {nome} é de R$ {salariobruto}, e salário final com desconto do INSS R$ {salariofinal}')