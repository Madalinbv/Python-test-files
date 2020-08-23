import csv

with open("/Users/madalinrauch/IdeaProjects/Python-test-files/Real_project/Emissions.csv", "rt") as file_read:
    data=csv.reader(file_read)
    result = {}
    for raw in data:
        key = raw[0]
        result[key] = list(raw [1:])
for item in result:
    print(item + " - " + str(result[item]))
file_read.close()