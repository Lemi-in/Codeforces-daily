
word = input()
if len(word) == 1:
    result = word.swapcase()
elif word.isupper() or (word[1:].isupper() and word[0].islower()):
    result = word.swapcase()
else:
    result = word

print(result)
