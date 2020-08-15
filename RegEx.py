# import regular expressions
import re
text = "random string. MyName123@website.com . some more random text Your.Name_888@company.net "

pattern = re.compile("[a-zA-Z0-9\.\-\_]+@+[a-zA-Z0-9]+\.+[a-zA-Z]+")
#[ABC] - any letter capital
#[a-zA-Z] + the + makes it go further
#[a-zA-Z0-9]+@+[a-zA-Z0-9]+\.+[a-zA-Z]+ - email address
#stops at first match

result = pattern.search(text) #searches the first occurence
result = pattern.findall(text) #finds all
print(result)