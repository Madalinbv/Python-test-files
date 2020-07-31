jabber = open("/Volumes/Sandisk/Download/cursuri/python/sample.txt", 'r')

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')
    #print(line)

jabber.close()
# jabber = open("sample.txt",'r')
# # jabber = open("C:\\Documents and Settings\\tim\\My Documents\\sample.txt", 'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()

# with open("/Volumes/Sandisk/Download/cursuri/python/sample.txt", 'r') as jabber:
#     for line in jabber: #for each line
#         if "JAB" in line.upper():
#             print(line, end='')
#
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line: #process until there are no more lines to read
#         print(line, end='')
#         line = jabber.readline()
#
# with open("/Volumes/Sandisk/Download/cursuri/python/sample.txt", 'r') as jabber:
#     lines = jabber.readlines() #reading each line
# print(lines)
#
# for line in lines:
#     print(line, end='')
# with open("/Volumes/Sandisk/Download/cursuri/python/sample.txt", 'r') as jabber:
#     lines = jabber.readlines() #gives a list of strings
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')
#
# with open("sample.txt", 'r') as jabber:
#     lines = jabber.read()
#
# for line in lines[::-1]:
#     print(line, end='')
