

def odd (mylist):
    n = int(input())
    if n == 0:
        return mylist
    if n % 2 == 1:
        mylist.append(n)
    return odd(mylist)

mylist = []
mylist = odd(mylist)
print(mylist)