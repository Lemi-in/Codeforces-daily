t = int(input())

for _ in range(t):
    numStrings = int(input())
    strings = []
    for _ in range(numStrings):
        s = input()
        strings.append(s)
    
    stringsSet = set(strings) # O(1) lookup
    # if it was a list, it would be O(n) lookup
    result = '' 

    for string in strings:
        found = False
        for start in range(len(string)):
            firstHalf = string[:start + 1]
            secondHalf = string[start + 1:]

            if firstHalf in stringsSet :
                if secondHalf in stringsSet:
                    found = True
                    break
            
        result += '1' if found else '0'

    print(result)
