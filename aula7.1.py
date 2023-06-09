"""
TIPOS DE DADOS

Variável = espaço na memoria que armazena informações tempórarias
padrão snackCase (nomeAluno, notaBimestre, relatoriodeVendas_janeiro

nome validos da variavel
* letras minúsculas sem acentos, caso exista duas palavras na variável
      ex: nome = 'Mariana', distancia = 45.58, bimestre1, _teste = 'dfaf'

nome invalidos da variavel
    ex: 1bimestre, @teste, (nome)
Tipos de dados para escrever python o "tipo" de informação que será armazanada na variável criada

Variável nome Mariana é do tipo <class 'str'>
Variável namorando True é do tipo <class 'bool'>
Variável idade 26 é do tipo <class 'int'>
Variável peso 80.0 é do tipo <class 'float'>
Variável alunos ['Mariana', 'Jonatas', 'Caio'] é do tipo <class 'list'>

"""

nome = 'Mariana'
namorando = True
idade = 26
peso = 80.00
alunos = ['Mariana', 'Jonatas', 'Caio']

print("Variável nome", nome, "é do tipo", type(nome))
print("Variável namorando", namorando, "é do tipo", type(namorando))
print("Variável idade", idade, "é do tipo", type(idade))
print("Variável peso", peso, "é do tipo", type(peso))
print("Variável aluno", aluno, "é do tipo", type(aluno))
