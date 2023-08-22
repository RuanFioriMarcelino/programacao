""" 26) Faça um programa que leia e valide as seguintes informações:
    a. Nome: maior que 3 caracteres;
    b. Idade: entre 0 e 150;
    c. Salário: maior que zero;
    d. Sexo: 'f' ou 'm';
    e. Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres). """



nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite o sexo 'm' para masculino, 'f' para feminino: ")
civil = input("Estado civil: s, c, v, d: ")

if len(nome) > 3:
    print("Nome com mais de 3 caracteres.")

if idade > 0 and idade < 150:
    print("Idade entre 0 e 150.")

if salario > 0:
    print("Salário maior que 0 !")

else:
    print("Salário menor ou igual a 0!")

if sexo == 'm' or sexo == 'f':
    if sexo == 'm':
        print("Sexo Masculino")
    else:
        print("Sexo Feminino")
else:
    print("Sexo não informado corretamente!")

if civil == 's' or civil == 'd' or civil == 'c' or civil == 'v':
    if civil == 'c':
        print("Estado civil: Casado")
    if civil == 'v':
        print("Estado civil: Viuvo")
    if civil == 's':
        print("Estado civil: Solteiro")
    if civil == 'd':
        print("Estado civil: Divorciado")
else:
    print("Informação invalida!")