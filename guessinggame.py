import random

highest=1000
answer=random.randint(1,highest)
print(answer) #TODO: remove after testing
print("please guess between 1 and {}:".format(highest))
guess=0 #initialize to any number that is not equal
while guess!= answer:
    guess=int(input())

    if guess==0:
        print("you asked for exit. The correct number was {}".format(answer))
        break
    if guess==answer:
        print ("you guessed it")
    if guess < answer:
        print ("too low")
    else:
        print ("too high")
# if guess< answer:
#     print("too low")
#     guess = int(input())
#     if guess==answer:
#         print("well done")
#     else:
#         print("not correct")
# elif guess>answer:
#     print("too high")
#     guess = int(input())
#     if guess==answer:
#         print("well done")
#     else:
#         print("not correct")
# else:
#     print("you got it")
