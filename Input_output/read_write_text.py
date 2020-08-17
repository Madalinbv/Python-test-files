# jabber = open("/Users/madalinrauch/IdeaProjects/Python-test-files/Input_output/sample.txt", 'r')
# # 'r' for read file
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end=' ')
# # you need to close the file, too
# jabber.close()
#
# with open("/Users/madalinrauch/IdeaProjects/Python-test-files/Input_output/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end=' ')
#
# with open('sample.txt','r') as jabber:
#     line=jabber.readline()
#     while line:
#         print(line, end='')
#         line=jabber.readline()

with open('sample.txt', 'r') as jabber:
    lines=jabber.readlines()
print(lines)
for line in lines:
    print(line, end='')