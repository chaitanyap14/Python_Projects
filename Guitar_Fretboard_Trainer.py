import random

print("===== FRETBOARD TRAINER =====")

print("\nIf you can complete level 2, 3, and 4 at 100bpm, you're done.")

notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]


#Level select
print("0. Exit\n1. One note\n2. One note + metronome\n3. Two notes + metronome\n4. Random notes + metronome\n")

while(True):
    option = int(input("\nSelect level: "))
    if option in range(0,5):
        if(option == 0):
            print("\nBye!")
            break
        elif(option == 1):
            print("\nPlay the following note on every string as slow as you want. If you can play up and down the strings 3 times without any mistakes, then you can move on to the next note.")
            print(random.sample(notes, 1))
            continue
        elif(option == 2):
            print("\nPlay the following note on every string. Start with 40bpm. If you can play every note at that bpm comfortably without making any mistakes, then increase the bpm.")
            print(random.sample(notes, 1))
            continue
        elif(option == 3):
            print("\nPlay the following 2 notes. One going down, and one going up. Start with 40bpm. If you can play every note at that bpm comfortably without making any mistakes, then increase the bpm.")
            print(random.sample(notes, 2))
            continue
        elif(option == 4):
            print("\nPlay the following notes alternating up and down. Start with 40bpm. If you can play all the notes in any random order comfortably without any mistakes, then increase the bpm.")
            print(random.sample(notes, 12))
            continue
    else:
        print("\nInvalid input")
        continue


