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
while resp and tentativa <= 3:
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
        tentativa = tentativa + 1