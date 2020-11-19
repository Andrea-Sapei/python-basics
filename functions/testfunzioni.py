def my_function():
      print("Hello from a function")
      how = input("How are you? ")
      return how


how = my_function()     #si dichiara how e lo si assegna a my_function(), la funzione non prende input ma da output

print("I'm {} too".format(how))
