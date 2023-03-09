voltas = int(input("Informe um número inteiro: "))
total = list("")
for i in range(0,voltas+1):
    if i == 0 or i==1:
        total.append(i)
    else:
        total.append(total[i-1]+total[i-2])
if voltas in total:
    print(f"O valor informado, {voltas}, pertence a sequencia!")
else:
    print(f"O valor informado, {voltas}, não pertence a sequencia!")