import re

pattern1= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string1= input("Enter a valid email address")


validator= pattern1.search(string1)

if validator != None:
    print("Email address is valid")
else:
    print("Email address is not valid")


