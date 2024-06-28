t = int(input())

for _ in range(t):
    n = int(input())
    
    p1 = input().split()
    p2 = input().split()
    p3 = input().split()
    
    wordC = {}
    words = [p1, p2, p3]
    scores = [0, 0, 0]
    

    for i in range(3):
        for word in words[i]:
            if word not in wordC:
                wordC[word] = 0
            wordC[word] += 1
    

    for i in range(3):
        for word in words[i]:
            if wordC[word] == 1:
                scores[i] += 3
            elif wordC[word] == 2:
                scores[i] += 1
    
    print(scores[0], scores[1], scores[2])
