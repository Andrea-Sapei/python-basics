

print("Questo programma conta i fattoriali fino a un numero")
nmax=int(input("Inserire numero: "))



for x in range(0,nmax+1):
    total=1
    if nmax>1:
        for num in range(1,x+1):
            total=total*num
        print(str(x)+ ": " + str(total))
    elif nmax==0:
        total=1
        print("Il fattoriale è {}".format(total))
