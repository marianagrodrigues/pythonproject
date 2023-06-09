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