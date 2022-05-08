'''
O código imprime todos os números que se somados ao inverso do valor de seus dígitos, esse não 
podendo iniciar em zero, resulta em um número ímpar menor que 1 milhão 
'''


for numero in range(1000000):
    #Coloca cada dígito de n em um espaço de um vetor
    vetor = [i for i in str(numero)]
    #Cria um vetor reverso
    vetor_inverso = vetor[::-1]
    #Cria uma string que junta os dígitos do vetor reverso
    numero_inverso = "".join(vetor_inverso)
    #Verifica se a soma é maior que 1 milhão ou par ou se o número ao contrário inicia com zero e ingora
    if (numero + int(numero_inverso) > 1000000) or ((numero + int(numero_inverso)) % 2 == 0) or int(vetor_inverso[0]) == 0:
        continue
    print(numero)
    
