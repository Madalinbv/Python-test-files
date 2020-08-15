# organized data
# fast e.g. contacts list
from collections import OrderedDict

groceries = {'bananas': 5,
             'oranges': 3,
             'key': 'value'
             }

print(groceries)
contacts = {'first': {'phone': '0745707177', 'email': 'email@website.com'},
            'second': '0769012306'}
print(contacts.get('first'))

word_count = {
    'I': 1,
    'like': 1,
    'the': 3
}

word_count['aaron'] = 2
# sentence = "i like the name aaron because the name aaron is the best"
# word_counts={}
# dict.items()
# dict.keys()
# dict.values()
# dict.pop(key) - taking the item out (delete), and retrieve it (it can be used in print
# dict.popitem() - pop last element added - return a tuple when printed
# dict[key] = value - add item
# dict.clear() - clears dictionary
print(sorted(list(word_count.values())))