def addizione(a,b):
    c=a+b
    print("Il risultato è {}".format(c))
    return c

def sottrazione(a,b):
    c=a-b
    print("Il risultato è {}".format(c))
    return c

def moltiplicazione(a,b):
    c=a*b
    print("Il risultato è {}".format(c))
    return c

def divisione(a,b):

    if b==0:
        print("Impossibile dividere per 0")
    else:
        c=a/b
        print("Il risultato è {}".format(c))
        return c



print("Questo programma effettua operazioni")

a=int(input("Inserire primo numero: "))
b=int(input("Inserire secondo numero: "))


#volevo aggiungere un check alla scelta dal menù delle operazioni, ma andava in loop infinito
#anche quando la scelta era valida

print("")
print("|1-addizione|2-sottrazione|3-moltiplicazione|4-divisione|")
scelta=int(input("Quale vuoi fare? 1-4: "))

if scelta==1:
    risultato=addizione(a,b)
elif scelta==2:
    risultato=sottrazione(a,b)
elif scelta==3:
    risultato=moltiplicazione(a,b)
elif scelta==4:
    risultato=divisione(a,b)
else:
    print("Scelta invalida"); 




        
