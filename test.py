name = input("what is your name? ")
age = int(input ("what is your age "))

print("hello {}".format(name))
if 18<=age<31:
    print("welcome to our our holiday, {0}".format(name))
else:
    print("I am sorry, this holiday is not for you")