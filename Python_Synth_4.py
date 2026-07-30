hz = input("Please enter the Hz you want to switch octaves from. ")

try:
    print(hz)
    hz = float(hz)
    count = 0
    while count < 2:
        hz *= 2
        count += 1
        print(hz)
except:
    print("We cant use that!")