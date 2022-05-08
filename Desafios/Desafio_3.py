'''
Algoritmo que recebe um numero n, e uma quantidade x de numeros e retorna a(s) possibilidade(s) de soma que sejam iguais
à n e que tenham o menor numero de elementos possíveis 
'''

import sys

#Recebe o número n
numero_objetivo = int(input("Digite o número: "))
vetor_numeros = []

#Recebe um número n de números até o usuário digitar 0
while True: 
    novo_numero = int(input("Digite um número para adicionar ao vetor, digite 0 para parar de adicionar: "))
    if novo_numero == 0:
        break
    #Verifica se o número já foi informado
    if novo_numero in vetor_numeros:
        print("Número já está no vetor, adicione outro número")
        continue
    vetor_numeros.append(novo_numero)

vetor_numeros.sort()

i = 0
vetor_possibilidades = []
matriz_possibilidades = []

#Pra cada repeticao cria um vetor de possibilidades iniciando com um elemento diferente do vetor de numeros informado pelo usuário
for j, numero in enumerate(vetor_numeros):

    vetor_possibilidades = []
    soma = numero_objetivo
    soma -= numero
    vetor_possibilidades.append(numero)
    i = 0
    while True:
        
        #Para o laco quando chegar ao ultimo elemento do vetor de numeros informado
        if i == len(vetor_numeros):
            break

        soma -= vetor_numeros[i]

        #Verifica se o número armazenado no indice i somado aos outros elementos do vetor_possibilidade gera uma soma igual 
        #ou menor ao numero_objetivo e adiciona ao vetor_possibilidade
        if soma >= 0:
            vetor_possibilidades.append(vetor_numeros[i])
        #Verifica todos os numeros do vetor e remove o ultmo elemento do vetor_possibilidade se nenhuma possibilidade atinjgir o numero_objetivo, repete o processo 
        #até achar uma combinação que atinja o objetivo ou verificar todas elas
        else: 
            soma += vetor_numeros[i]
            for k, numeroSoma in enumerate(vetor_numeros):
                soma -= numeroSoma
                if soma == 0:
                    vetor_possibilidades.append(numeroSoma)
                    matriz_possibilidades.append(vetor_possibilidades)
                    vetor_possibilidades
                    soma = numero_objetivo 
                    i += 1
                    break
                else:
                    soma += numeroSoma
                    if k == (len(vetor_numeros) - 1):    
                        soma += vetor_possibilidades[-1]
                        vetor_possibilidades.pop()
                        i += 1
        
        #A soma será numero_objetivo quando o 1º numero do vetor não permitir nenhuma possibilidade de soma, entao ele parte pra proxima repeticao
        if soma == numero_objetivo:
            break

        #Verifica se a soma do vetor n é igual ao número n definido e coloca na matriz de possibilidades
        if soma == 0:
            matriz_possibilidades.append(vetor_possibilidades)
            vetor_possibilidades = [vetor_numeros[j]]
            soma = numero_objetivo - vetor_numeros[j]
            i += 1
            continue   

#Organiza os vetores da matriz em ordem
for vetor in matriz_possibilidades:
    vetor.sort()

matriz_resultado = []

#Adiciona a uma nova matriz apenas um vetor de cada se existirem duplicatas
for i,vetor in enumerate(matriz_possibilidades):
    if not(vetor in matriz_resultado):
        matriz_resultado.append(vetor)

#Define qual o menor tamanho de vetor na matriz
menor_len_vetor = sys.maxsize
for vetor in matriz_resultado:
    if len(vetor) < menor_len_vetor:
        menor_len_vetor = len(vetor)

#Verifica quaais vetores possuem o menor tamanho 
matriz_final = []
for vetor in matriz_resultado:
    if len(vetor) == menor_len_vetor:
        matriz_final.append(vetor)

#Imprime os resultados
print(f"Número da soma: {numero_objetivo}")
print("Menor(es) possibilidade(s) de soma: ")
for vetor in matriz_final:
    print(vetor)
