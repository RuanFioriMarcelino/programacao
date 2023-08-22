"""34) Faça 4 listas:
A. Filmes
B. Jogos
C. Livros
D. Esporte
a. Adicione no mínimo 2 itens em cada lista.
b. Crie uma lista das 4 listas criadas acima.
c. Acesse (mostrar) algum item da lista livros.
d. Remova um item da lista esporte."""

filme = ['dora', 'invocacao do mal']
jogo = ['cs', 'pubg']
livro = ['Café Com Deus Pai', 'É Assim Que Acaba']
esporte = ['volei', 'tenis de mesa']

tudo = filme + jogo + livro + esporte
print(livro[1])
esporte.remove('tenis de mesa')