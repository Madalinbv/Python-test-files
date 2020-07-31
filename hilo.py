low=1
high=1000

print ("please think of a number between {} and {}".format(low,high))
input("press enter to start")
guesses =1
while low != high:
    print("\t guessing in the range of {} to {}".format(low,high))
    guess=low + (high-low)//2
    high_low=input("my guess is {}. Should I guess higher or lower? "
    "enter c if guess is correct "
                   .format(guess)).casefold()
    if high_low=="h":
        #guess higher. The low end of the range becomes 1 greater than the guess
        low=guess+1
    elif high_low=="l":
        #guess lower. the high end of the range becomes one less than the guess
        high=guess-1
    elif high_low=="c":
        print("i got it in {} guesses!".format(guesses))
        break
    else:
        print("please enter h, l or c")
   # guesses = guesses + 1
    guesses += 1
else:
    print("you thought of the number {}".format(low))
    print("i got it in {} guesses!".format(guesses))
