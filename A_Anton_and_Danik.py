n = int(input())
games = input()
anton = 0
danik = 0
if games.count('A') > games.count('D'):
    print('Anton')
elif games.count('A') < games.count('D'):
    print('Danik')
else:
    print('Friendship')