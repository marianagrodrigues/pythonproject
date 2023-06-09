def exibir_formulario():
    print("Formulário")
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")

    print("\nDados do formulário:")
    print("Nome:", nome)
    print("Data de Nascimento:", data_nascimento)
    print("CPF:", cpf)
    print("Endereço:", endereco)

exibir_formulario()
