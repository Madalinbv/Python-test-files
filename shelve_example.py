import shelve
#with shelve.open('shelfTest') as fruit:
fruit = shelve.open('shelfTest')
fruit['orange']="a sweet, orange, citrus fruit"
fruit["apple"]="good for cider"
fruit["lemon"]="a sower one"
fruit["grape"]="one for wine"
fruit["lime"]="super-sower"
#
# print(fruit["lemon"])
# print(fruit['grape'])
# fruit['lime']='great with tequila'
# for snack in fruit:
#     print(snack+':'+fruit[snack])
#
# while True:
#     dict_key = input('please enter a fruit:')
#     if dict_key == 'quit':
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         #description = fruit.get(dict_key, "we don't have a " + dict_key)
#         print(description)
#     else:
#         print("we don't have a "+dict_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)
print(fruit.values())
for f in fruit.items():
    print(f)
print(fruit.items())
fruit.close()

#print(fruit)