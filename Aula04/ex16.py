""" 16) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
conversão.
 """
print("Digite 's' para sim e 'n' para não !!!")
respf = str(input("Você deseja converter a temperatura de Fahrenheit para Celsius? "))
if respf == "s":
    fahrenheit=float(input("Digite o valor em fahrenheit: "))
    celsiusC=(fahrenheit-32)/1.8
    print(f'Temperatura em celsius {celsiusC}')
else:
    respc = input("Você deseja converter a temperatura de Celsius para Fahrenheit? ")
    if respc == "s":
        celsius =float(input("Digite o valor em celsius: "))
        fahrenheit = celsius * 1.8 + 32
        print(f'Temperatura em fahrenheit {fahrenheit}')
    
