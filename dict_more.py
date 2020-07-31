fruit = {"orange":"a sweet orange",
         "apple":"good for cider",
         "lemon":"a sower one",
         "grape":"one for wine",
         "lime":"super-sower"}
print(fruit)
veg={"cabbage":"every child's favourite",
     "sprouts":"mmm, lovely",
     "spinach":"can I have more fruit, please?"}
print(veg)
veg.update(fruit)
print(veg)

print(fruit.update(veg))
print(fruit)
nice_and_nasty=fruit.copy()
print(nice_and_nasty)
nice_and_nasty.update(veg)
print(nice_and_nasty)