print("This programs multiplies two numbers, but in an unnecessarily complicated way")

a=int(input("Insert first number: "))
b=int(input("Insert second number: "))

k=0
result=0

while k<b:
    result=result+a
    k=k+1

print("The result is {}".format(result))
