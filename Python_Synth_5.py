volume = int(input("Please enter a volume BETWEEN 0 and 11. "))

try:
    for i in range (volume):
        print("#", end = "") 
    print( )
except:
    print("We can't use that!")