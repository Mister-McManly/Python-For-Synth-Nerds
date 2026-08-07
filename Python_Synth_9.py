BPM = float(input("What is the beats per minute of the song you are using? "))
Beats = float(input("How many beats are in the song you are using? "))

try:
    Min = float(Beats // BPM)

    Seconds =float((Beats % BPM) * 60 / BPM)

    print("Your song is", str(Min) + " minutes long, and", str(Seconds) + " seconds long.")
except:
    print("We can't use that!")