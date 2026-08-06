import random

drum = []

for i in range(8):
    if random.random() < 0.5:
        drum.append("1")
    else:
        drum.append("0")

for item in drum:
    if item == "1":
        print("Hit")
    else:
        print("Rest")