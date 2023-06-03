#acesso ao sistema
login = "admin"
senha = 123456

loginDigitado = input ("Digite seu login: ")
senhaDigitada = int(input ("Digite a senha: "))

if loginDigitado == login:
    print ("Acesso permitido...")

else:
    print ("Mete o pé...")
