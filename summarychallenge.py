choice = "-"
while choice != "0":
    if choice in "123":
        print("you chose {}".format(choice))
    else:
        print("please choose the option from the list:")
        print("1\t Learn Python")
        print("2\t Learn Java")
        print("3\t wimming")
        print("0\t Exit")
    choice = input()

