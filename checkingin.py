parrot = "norwegian blue"

letter = input("letter:")

if letter in parrot:
    print("{} is on {}".format(letter, parrot))
else:
    print("i don't need that letter")