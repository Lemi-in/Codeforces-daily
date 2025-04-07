#author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint

rand = randint(1, 10**5)
def ran(num): return num ^ rand
def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
 
def solve():
    n, q = ints()
    a = li()
    queries = []
    
    results = []
    for k, x in queries:
        count = 0
        for i in range(k):
            if x > a[i]:
                count += 1
        results.append(count)
    
    
 
t = it()
for _ in range(t):
    solve()













#Note.
# Note that after the strongest athlete is at the beginning of the queue, only he will win. The strongest athlete will be at the beginning of the queue no more than after the n
# -th round. Let's simulate the first n
#  rounds, if the j
# -th athlete won in the i
# -th round, then we will write down the i
#  number for him. Now, to answer the query (i,k)
# , it is enough to find the number of wins of the i
#  athlete in rounds with numbers j≤k
# , and if k>n
# , and the strength of the i
#  athlete is equal to n
# , then add to the answer another k−n
# .

# The complexity of the solution is O(n+qlog(n))
# .




















#     In the late 19th century, Empress Taytu Betul led a victorious campaign, capturing N
#  Italian soldiers after a decisive battle. Each of these prisoners possesses a certain level of combat skill.

# The Empress has gathered Q
#  warriors for evaluation. As they prepare for future battles, she wishes to assess their strength against the captured soldiers. To do so, she devises a test.

# The N
#  prisoners have been arranged in a fixed order, determined by the Empress's generals. This order is predefined, and the combat skill values are given in an integer array A
# , where Ai
#  represents the combat skill value of the ith
#  prisoner.

# Each of the Q
#  warriors will be tested separately. For a given warrior:

# The first K
#  prisoners from the order are selected.
# The warrior, with combat skill X
# , will engage in duels against each of these K
#  prisoners individually.
# The outcome of each duel follows these rules:

# If the warrior's combat skill X
#  is greater than the prisoner's combat skill, the warrior wins that duel.
# If the warrior's combat skill X
#  is equal to or less than the prisoner's combat skill, the warrior does not win that duel.
# For each warrior, determine how many of the first K
#  prisoners they can defeat.

# Input
# You are given T
#  test cases (1≤T≤100
# ).

# For each test case:

# The first line contains two integers N
#  and Q
#  (1≤N,Q≤105
# ) – the number of captured Italian soldiers and the number of Ethiopian warriors, respectively.
# The second line contains N
#  integers A1,A2,…,AN
#  (1≤Ai≤109
# ) – the combat skills of the captured Italian soldiers, given in their fixed order of arrangement.
# The next Q
#  lines each contain two integers K
#  and X
#  (1≤K≤N
# , 1≤X≤109
# ) – meaning the warrior with strength X
#  will fight the first K
#  prisoners from this ordered list.
# The sum of N
#  and Q
#  over all testcases does not exceed 2×105
# .

# Output
# For each query, output a single integer – the number of prisoners among the first K
#  that the warrior can defeat.

# Example
# InputCopy
# 3
# 5 3
# 3 1 4 1 5
# 2 2
# 4 3
# 5 5
# 3 2
# 10 20 30
# 1 15
# 3 25
# 5 3
# 10 20 30 40 50
# 5 5
# 5 1
# 5 9
# OutputCopy
# 1
# 2
# 4
# 1
# 2
# 0
# 0
# 0
# Note
# For the first test case, 3
#  warriors are tested:

# The first warrior will fight the first 2
#  prisoners, and has a combat skill value of 2
# . And he will only be able to defeat the second prisoner. So in total he will only be able to defeat 1
#  prisoner.
# The second warrior will fight the first 4
#  prisoners, and has a combat skill value of 3
# . And he will only be able to defeat the second and the fourth prisoner. So in total he will only be able to defeat 2
#  prisoners.
# The third warrior has to fight all 5 prisoners. His combat skill value is 5
# , which is enough to defeat every prisoner expect the last prisoner. Therefore, he will be able to defeat 4
#  prisoners.