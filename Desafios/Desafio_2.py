
#Define o mínimo de alunos para a aula iniciar
minimo_alunos = int(input("Digite o nº mínimo de alunos para que a aula seja iniciada: ")) 

i = 1 
#Registra a quantidade de alunos que chegou no horário
normal = 0

print("Digite o tempo de chegada dos alunos seguindo o esquema:\nAtrasado = (tempo de atraso)\nEm ponto: 0\nAdiantado: -(Tempo de adiantamento)\nSair: S")

#Laço que repete até o usuário digitar s e verifica se o tempo do aluno é normal ou atrasado
while True:
    tempo_chegada = input(f"{i}° aluno: ")
    if tempo_chegada.upper() == "S":
        break
    elif int(tempo_chegada) <= 0 :
        normal += 1
    i += 1

#Printa "Aula cancelada" se o número de aluno for menor que o mínimo de alunos, senão "printa Aula normal"
if normal < minimo_alunos:
    print("Aula cancelada!")
else:
    print("Aula normal")
    