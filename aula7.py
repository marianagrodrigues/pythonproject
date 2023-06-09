# resumão
# comentario de uma linha
aluno = "Mariana"  # está parte não será interpretada

"""
DocString - pode ser usado como comentario de várias linhas

"""

# str - string

"""
O uso do caracter \ (barra invertida inform ao python para escrever o texto depois...

"""

print("o aluno\r esteve\"presente\"na aula")
print('o aluno esteve "presente" na aula')

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

"""
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

"""
Comandos condicionais
o if sempre espera uma reposta True, caso a condição seja False ele faz bloco else 
(pode ser que exista o bloco Elif que existe quando temosmais de uma condição possível)
"""
entrada = input("você quer entrar ou sair: ")
if entrada == 'entrar':
    print("você entrou...")
elif entrada == 'sair':
    print("Você saiu...")
else:
    print('Tem que escolhe uma resposta...')

"""
Operadores Relacionais
"""
print("2 > 1: ", 2 > 1)
print("1 > 2", 1 > 2)
print("2 = 2: ", 2 == 2)
print("2 > 2: ", 2 > 2)
print("a != b: ", 'a' != 'b')  # ! -> ele é o NÃO e = -> é igual (não-igual = diferente)

"""
operadores and / or / not

"""
login = "ADMIN"
senha = 123
# upper converte para MAIÚSCULA
# lower converte para MINÚSCULA


"""
if loginDigitado == login:
    print("Login Correto...")
if senhaDigitada == senha:
    print("senha correta, está logado!")
    
"""

"""
if senha==senhaDigitada and login == loginDigitado:
    print("Logado com sucesso")
else:
    print ("mete o pé meu anjo...")
"""
resp = True
tentativa = 1
while resp and tentativa <=3:
    loginDigitado = input("Informe login: ").upper()
    if login == loginDigitado:
        senhaDigitada = int(input("Informe senha: "))
        if senha == senhaDigitada:
            print('acesso permitido')
            resp = False
        else:
            print("senha incorreta")
    else:
        print('login errado / não cadastrado')
        print('tentativa: ', tentativa, "de 3")
        tentativa = tentativa +1
