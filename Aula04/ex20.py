""" 20) Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos. """

idade=int(input("Digite sua idade: "))
tempo=int(input("Digite quantos anos de serviço: "))

if idade >= 65:
    print("Cidadão apto a se aposentar.")
elif tempo >= 30:
    print("Cidadão apto a se aposentar.")
elif idade >= 60 and tempo >= 25:
    print("Cidadão apto a se aposentar.")
else:
    print("Cidadão não está apto a se aposentar")
