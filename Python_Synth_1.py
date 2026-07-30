Beats = input("How many beats do you want to have? ")
try:
    beats_int = int(Beats)
    for i in range (0, beats_int):
        if i % beats_int == 0:
            print("CLICK")
        else:
            print("click")
except:
    print("We can't use that!")
    
