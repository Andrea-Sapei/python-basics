total=1

print("Questo programma fa il fattoriale di un numero")
nmax=int(input("Inserire numero: "))



if nmax>1:
    for num in range(1,nmax+1):
        total=total*num
    print("Il fattoriale è {}".format(total))
elif nmax==0 or nmax==1:
    total=1
    print("Il fattoriale è {}".format(total))
else:
    print("Il numero non ha un fattoriale")


