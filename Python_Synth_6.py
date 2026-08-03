notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

indexunfin = input("Please enter the note you would like to start at: ")
try:
    indexfin = notes.index(indexunfin.upper())

    for i in range(12):
        index = (indexfin + i) % 12
        print(notes[index], end=" ")
    print()
except:
    print("We can't use that!")