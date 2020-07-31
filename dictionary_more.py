a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
a['doughnut'] = 'snack'
print(a)

a = {'one': 1, 'two': 'to', 'three': 3.0, 'four': [4,4.0]}
print(a)
# {'four': [4, 4.0], 'two': 'to', 'three': 3.0, 'one': 1}
# Update a dictionary
a['one'] = 1.0
print(a)
#{'four': [4, 4.0], 'two': 'to', 'three': 3.0, 'one': 1.0}
# Delete a single element
del a['one']
print(a)
#{'four': [4, 4.0], 'two': 'to', 'three': 3.0}
# Delete all elements in the dictionary
a.clear()
print(a)
#{}
# Delete the dictionary
del a
#print(a)
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Put all keys of `dict1` in a list and returns the list
dict1.keys()
#dict_keys(['c', 'd', 'a', 'b'])
# Put all values saved in `dict1` in a list and returns the list
dict1.values()
#dict_values([3, 4, 1, 2])

#dict_variable = {key:value for (key,value) in dictonary.items()}

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)
dict1_keys = {k*2:v for (k,v) in dict1.items()}
print(dict1_keys)
# Consider the following problem, where you want to create a new dictionary where the key is a number divisible by 2 in a
# range of 0-10 and it's value is the square of the number.
# Let's see how the same probem can be solved using a for loop and dictionary comprehension:

numbers = range(10)
# new_dict_for = {}
#
# # Add values to `new_dict` using for loop
# for n in numbers:
#     if n%2==0:
#         new_dict_for[n] = n**2
#
# print(new_dict_for)

# Use dictionary comprehension
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_comp)

#nested
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}