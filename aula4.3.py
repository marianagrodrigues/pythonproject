print ("-------- ACESSO AO SISTEMA ----------")

#login = "marianarodrigues"
#senha = 123456

loginDigitado = input ("Login: ")
senhaDigitada = (input("Senha: "))

print ("Login: ")
print ("Senha: ")

print ('-' * 20)

resp = 's'

while resp == 's':
    print ('usuario logado...')
    resp = input ("Logoff ? [s] [n]")

    print ("usuario deslogado")
