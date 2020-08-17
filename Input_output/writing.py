# cities = ["brasov", "Bucuresti", "Predeal","Ploiesti" ]
# with open("orase.txt", "w") as city_file:
#     for city in cities:
#         print(city, file=city_file, flush=True) # flush - immediately write the data to the file
# cities = []
# with open ('orase.txt', 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n')) # striping new line char
#
# print(cities)

imelda = "More Mayhem", "Imelda MAy", "2011", (
    (1, "Pulling the Rug"), (2,"Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("imelda3.txt", 'a') as imelda_file: # a for append
    print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents) # evaluate contents

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks[1])
