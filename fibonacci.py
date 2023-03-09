
# Entrada de dados, salvando-a como Integer
voltas = int(input("Informe um número inteiro: "))

# Declarando a variavel de saída
total = list("")

# Loop com voltas, lembrando de realizar o +1, pois o python não executa a última volta em seu For
for i in range(0,voltas+1):
    #Teste para os 2 primeiros elementos, tendo em vista que são unicos
    if i == 0 or i==1:
        # Funcao append, adiciona um elemento a lista
        total.append(i)
    else:
        total.append(total[i-1]+total[i-2])

# Teste para verificar se o valor informado está na lista:
if voltas in total:
    print(f"O valor informado, {voltas}, pertence a sequencia!")
else:
    print(f"O valor informado, {voltas}, não pertence a sequencia!")