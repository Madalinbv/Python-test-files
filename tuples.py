# # # # # welcome="welcome to my nightmare","aclice",1975
# # # # # bad="bad company""bad company", 1974
# # # # # Given the tuple below that represents the Imelda May album "More Mayhem", write
# # # # # code to print the album details, followed by a listing of all the tracks in the album.
# # # # #
# # # # # Indent the tracks by a single tab stop when printing them (remember that you can pass
# # # # # more than one item to the print function, separating them with a comma).
# # # #
# # # # imelda = "More Mayhem", "Imelda May", 2011, (
# # # #     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
# # # #
# # # # print(imelda)
# # # #
# # # # title, artist, year, tracks = imelda
# # # #
# # # # print(title)
# # # # print(artist)
# # # # print(year)
# # # # print("tracks:")
# # # # for i in tracks:
# # # #     track_num, track_name = i
# # # #     print (track_num,"\t" ,track_name)
# # #
# # # cast = ['Cleese', 'Idle', 'Gilliam', 'Jones', 'Palin', 'Chapman']
# # #
# # # print(cast.sort())
# # #
# # #
# # flowers = [["rose", "red"],
# #            ["snapdragon", "white"],
# #            ["daisy", "white"],
# #            ["lily", "yellow"]
# #            ]
# #
# # second_flowers = flowers
# # print(second_flowers)
# # print("#"*10)
# # print(second_flowers[1])
# # print("#"*10)
# # second_flowers[1] = ["lilac", 'purple']
# # print(second_flowers[1])
# # print("#"*10)
# # second_flowers[1][1] = 'pink'
# # print(second_flowers)
# # print("#"*10)
# # print(flowers)
# numbers = range(13)
# print(numbers)
# print("#"*10)
#
# new_range = numbers[1::2]
# print(new_range)
# for i in new_range:
#     print(i, ', ')
# imelda = 'More Mayhem', 'Imelda May', 2011, [
#     (1, 'Pulling the Rug'),
#     (2, 'Psycho'),
#     (3, 'Mayhem'),
#     (4, 'Kentish Town Waltz')]
#
# imelda[3].append(5, 'All For You')
# print(imelda[3])
t=(0,1,2,3,4,5,6,7,8,9)
print (t[11:0:-2])
person1=('nancy-pants', 25, 'pizza')
person2=('nancy-pants2', 32, 'french fries')
person = [person1, person2]
for name, age, favfood in person:
    print(name)
    print(age)
    print(favfood)
    print()