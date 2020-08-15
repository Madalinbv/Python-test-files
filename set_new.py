l = [1,2,3,3,4,4,5,'abc',"abc"]
no_duplicate_set = set(l) #because sets contain unique items
print(no_duplicate_set, " as a set")
no_duplicate_list = list(no_duplicate_set)
print(no_duplicate_list,  " as a list") #back to list with no duplicates

lib1= {'harry potter','Hunger Games','lord of the rings'}
lib2= {'harry potter','romeo and juliet'}

all_books = lib1.union(lib2)
common_books = lib1.intersection(lib2)
diff = lib1.difference(lib2)
print(all_books, ' all books')
print(common_books,' intersection')
print(diff,' difference')

