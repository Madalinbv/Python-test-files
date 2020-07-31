# list_1=[]
# list_2= list()
# print("list 1 is {}".format(list_1))
# print("list 2 is {}".format(list_2))
# if list_1 == list_2:
#     print("the lists are equal")
#     print(list("the lists are equal"))
#even = [2,4,6,8]
# another_even = sorted(even, reverse=True)
#
# print(another_even == even)
# another_even.sort(reverse=True)
# print(even)
# print(another_even)
# odd = [1,3,5,7,9]
# numbers=[even,odd]
# for numbers_set in numbers:
#     print(numbers_set)
#     for value in numbers_set:
#         print(value)
# #print(numbers)
menu=[]
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

# print(menu)

for meal in menu:
    if not "spam" in meal:
        for ingredient in meal:
            print(ingredient)