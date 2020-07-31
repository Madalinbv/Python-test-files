# numbers = {
#     1: 'one',
#     3: 'three',
#     5: 'five',
#     7: 'seven',
#     9: 'nine',
# }
#
# print("I can count odd numbers in order")
# for key in numbers:
#     print(numbers[key])
# print('*'*8)
# numbers[8] = 'eight'
# numbers[2] = 'two'
# numbers[6] = 'six'
# numbers[4] = 'four'
#
# print()
# print("I can count to 9 in order")
# for key in numbers:
#     print(numbers[key], ' ', key)
#
# # If your code relies on the keys being sorted, sort them first
# print()
# print("I really can")
# for key in sorted(numbers):
#     print(numbers[key])
fruit = {"orange":"a sweet orange",
         "apple":"good for cider",
         "lemon":"a sower one",
         "grape":"one for wine",
         "lime":"super-sower"}

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"]="odd shaped apple"
# print(fruit)
# fruit["pear"]="great with tequila"
# print(fruit)
# #del fruit["lemon"]
# fruit.clear()
print(fruit)
# while True:
#     dict_key = input("please enter a fruit:")
#     if dict_key =="quit":
#         break
#     # description =fruit.get(dict_key, "we don;t hsve a"+dict_key)
#     # print(description)
#     if dict_key in fruit:
#         description =fruit.get(dict_key)
#         print(description)
#     else:
#          print("we don't have a {}".format(dict_key))
# for snack in fruit:
#     print(fruit[snack])
# for i in range (10):
#     for snack in fruit:
#         print(snack + ' is ' + fruit [snack])
#     print('='*40)
# ordered_key = list(fruit.keys())
# ordered_key.sort()
# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + " - " + fruit[f])
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
#
# print(fruit_keys)
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)
for snack in f_tuple:
    item, description = snack
    print (item + " is " + description)
print(dict(f_tuple))