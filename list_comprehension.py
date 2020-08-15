names = ['jennifer','susan', 'sophie', 'james']
l=[]
# for person in names:
#     l.append(person)
# print (l)
l = [person for person in names]
print (l)
print([person + ' dumped me ' for person in names])


movie_ratings={"interstellar":9, "Dark knight":8, "50 shades":3, "50 shades darker":2, "50 shades darkest":1}
l=[]
for movie in movie_ratings:
    if movie_ratings[movie] >6:
        l.append(movie)
print(l)
print([movie for movie in movie_ratings if movie_ratings[movie] > 6])