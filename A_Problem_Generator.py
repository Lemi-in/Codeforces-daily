t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    
    difficulty_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
    
    for problem in a:
        difficulty_count[problem] += 1
    
    problems_needed = 0
    for difficulty in 'ABCDEFG':
        if difficulty_count[difficulty] < m:
            problems_needed += (m - difficulty_count[difficulty])
    
    print(problems_needed)
