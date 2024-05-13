
try:
    t = int(input())
    n = 2 * t

    for _ in range(n):
        try:
            key = input()
            s = input()
            klist = list(key)
            slist = list(s)
            index = []
            for w in slist:
                if w in klist:
                    index.append(klist.index(w))
            index = [i + 1 for i in index]
            j = 1
            summ = 0
            for i in range(len(index) - 1):
                summ += abs(index[i] - index[j])
                j += 1
            print(summ)
        except EOFError:
            break
except EOFError:
    pass



