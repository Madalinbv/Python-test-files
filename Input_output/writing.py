cities = ["brasov", "Bucuresti", "Predeal","Ploiesti" ]
with open("orase.txt", "w") as city_file:
    for city in cities:
        print(city, file=city_file)