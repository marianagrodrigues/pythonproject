""""
Concatenar é misturar as informações em Strings literais com variáveis

"""
aluna1 = 'Mariana'
aluna2 = 'Yane'
aluna3 = 'Gabi'
imc = 80.6 / (1.64 ** 2)
turma = 'Trilha Python'

print(' * ' * 30)
print('A aluna: ', aluna1, 'faz o curso de: ', turma)
print(' * ' * 30)
print('A aluna: ', aluna2, 'faz o curso de: ', turma)

print(' * ' * 30)
# f-strings
# na variável imc utilizamos o controle de casas decimais
# .2f - 2 significa quantidade de casas decimais
print(f'a aluna: {aluna1} faz o curso de: {imc:.2f}')
