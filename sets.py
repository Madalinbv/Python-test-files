# # farm_animals={"sheep", "cow", "hen"}
# # print(farm_animals)
# #
# # for animal in farm_animals:
# #     print(animal)
# #
# #     print("*" * 50)
# #
# # wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# # print(wild_animals)
# #
# # for animal in wild_animals:
# #     print(animal)
# #
# # farm_animals.add("horse")
# # wild_animals.add("horse")
# # print(farm_animals)
# # print(wild_animals)
# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# #empty_set2.add("a")
#
# even=set(range(0,40,2))
# print(even)
# squares_tuple = (4,6,9,16.25)
# squares = set(squares_tuple)
# print(squares)

even = set(range(0,40,2))
print(even)
print(len(even))
print(sorted(even))

squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
print(sorted(squares))
print("even minus squares")
print(sorted((even.difference(squares))))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)
print("symmetric difference even minus square")
print(sorted(even.symmetric_difference(squares)))
#
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
# print(squares.union(even))
#
# print("--"*40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
# try:
#     squares.remove(8)
# except KeyError:
#     print("the item 8 is not in the set")
even = set(range(0,40,2))
print(even)
squares_tuple = (4,6,16)
squares = set(squares_tuple)
print(squares)

if squares.issubset(even):
    print("squares is a a sub set of even")
if even.issuperset(squares):
    print("even is a superset of squares")