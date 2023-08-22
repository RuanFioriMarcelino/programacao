""" 15) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
tela dizendo se está “quente”, “frio” ou “agradável”. """

temperatura = float(input("Qual a temperatura atual do ambiente?"))

if temperatura  <= 15 :
    print("Está frio!")
if temperatura  > 15 and temperatura <= 28 :
    print("Está agradável!")
if temperatura  > 28 :
    print("Está calor!")