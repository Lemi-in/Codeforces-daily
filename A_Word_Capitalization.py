s = input()
capitalized = s[0].upper()
rest = s[1:]
print(capitalized + rest)
#or we could just simply do this:
# print(s[0].upper() + s[1:])
#but I don't like that because it's not as readable as the first one