# PROGRAM TO GET THE MATCHING(same) CHARACTERS IN A STRING

string = input('enter somethig')
# noor
matchstring = []
for char in string:
    if (string.count(char)>1):
        matchstring.append(char)
print(matchstring)


