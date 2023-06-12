# saborPizza, tamanhoPizza, valorPizza, nomeCliente, diaSemana 

saborPizza = 'Calabresa', 'Mussarela', 'Frango', 'Marguerita'
tamanhoPizza = 'Média', 'Grande', 'Giga'
valorPizza = 39.90
nomeCliente = 'Mariana'
diaSemana = 'quinta', 'sexta'

# 2. As quintas ou as sextas comprando uma pizza grande de calabresa, o refri é grátis; se for quinta ou sexta o
# cliente comprando uma pizza grande de calabresa, ganha o refri se não for esses dias da semana, não ganha.

if diaSemana == 'quinta' and (diaSemana == 'sexta' or tamanhoPizza == 'Grande' or saborPizza == 'calabresa'):
    print('Sem promoção')
else: 
    print('[PROMO] - Refri grátis')