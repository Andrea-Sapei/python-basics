total=0

print("Questo programma somma tutti i numeri fino a un numero")
nmax=int(input("Inserire numero massimo: "))


for num in range(nmax+1):
    total=total+num

print("la somma è {}".format(total))
