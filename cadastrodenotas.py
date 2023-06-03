aluno = []
notas = ['','']
media = []
j = 0
print(len(notas)) #lenght = tamanho

resp ='s'
while resp == 's':
    cad_aluno = input('digite o nome do aluno')
    aluno.append(cad_aluno)
    i = 0

    media[j] = (notas[0] + notas[1])/2
    j = j + 1
    resp = input()


    while i<len(notas):
        notas[i] = float(input("Digite a nota: "))
        i = i + 1
    #print(aluno)
    resp = input("Continuar? [s] [n]")

for a in aluno:
    print("aluno(a): ", a)

for n in notas:
    print(n)


