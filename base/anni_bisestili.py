print("Questo programma calcola quali sono gli anni bisestili")

start=1
end=0

while start>end:
    start = int(input("Inserire anno di inizio: "))
    end = int(input("Inserire anno finale: "))
    if start>end:
        print("L'anno di inizio dev'essere prima di quello finale, reinserire")

while start<end:
    if start%4==0:
        if start%100==0:
            b=0
            if start%400==0:
                print(start)
        else:
            print(start)
    start=start+1

input("Premi enter per chiudere il programma")
        
