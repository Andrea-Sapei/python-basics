print("This programs divides two numbers, but in an unnecessarily complicated way")

a=int(input("Insert first number: "))
b=int(input("Insert second number: "))

k=0
result=a

if b!=0:
    if b>a:
        result=-b
        k=1
    else:
        while result>0:
            result=result-b
            k=k+1

    if result<0:
        print("The result is {}, with an excess of {}".format(k-1,-result))
    else:
        print("The result is {}".format(k))

else:
    print("Cannot divide by 0")


input("Press enter to end program")
