age=int(input("how old are you? "))

# if age >=16 and age<=65:
# if 16<=age<=65:
if age in range(16,66):
    print("have a good day at work")
else:
    print("enjoy your free time")

print("-"*80)

if age < 16 or age >65:
    print("enjoy your free time")
else:
    print("Have a good da15y at work")