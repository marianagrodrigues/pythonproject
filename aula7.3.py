"""
Coletar dados do teclado e formatar casas decimais
O comando input recebe valores vindos do teclado digitado pelo usuário
o input
"""
cidade = input('Digite o nome da cidade: ')
print(cidade, " - ", type(cidade))
print('-' * 30)
valor = float(input("Digite o valor do produto: "))
valor = valor / 3
print(f'valor de: {valor:.2f}', type(valor))