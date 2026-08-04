piano_chords = {
    "C": ["C", "E", "G"],
    "C Minor": ["C", "Eb", "G"],
    "C#": ["C#", "F", "G#"],
    "C# Minor": ["C#", "E", "G#"],
    "D": ["D", "F#", "A"],
    "D Minor": ["D", "F", "A"],
    "D#": ["D#", "G", "A#"],
    "D# Minor": ["D#", "F#", "A#"],
    "E": ["E", "G#", "B"],
    "E Minor": ["E", "G", "B"],
    "F": ["F", "A", "C"],
    "F Minor": ["F", "Ab", "C"],
    "F#": ["F#", "A#", "C#"],
    "F# Minor": ["F#", "A", "C#"],
    "G": ["G", "B", "D"],
    "G Minor": ["G", "Bb", "D"],
    "G#": ["G#", "C", "D#"],
    "G# Minor": ["G#", "B", "D#"],
    "A": ["A", "C#", "E"],
    "A Minor": ["A", "C", "E"],
    "A#": ["A#", "D", "F"],
    "A# Minor": ["A#", "C#", "F"],
    "B": ["B", "D#", "F#"],
    "B Minor": ["B", "D", "F#"]
}


used_scale = input("Please enter the key signature you would like to use. (You can only type C, C Minor, C#, C# Minor, D, D Minor, D#, D# Minor, E, E Minor, F, F Minor, F#, F# Minor, G, G Minor, G#, G# Minor, A, A Minor, A#, A# Minor, B, B Minor.) ")

try:
    print(piano_chords[used_scale])
except:
    print("We can't use that!")