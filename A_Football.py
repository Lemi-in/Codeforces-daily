n = int(input())
team_scores = [input() for _ in range(n)]

team_1 = team_scores[0]
team1_score = 1
team_2 = None
team2_score = 0

for team in team_scores[1:]:
    if team == team_1:
        team1_score += 1
    else:
        if team_2 is None:
            team_2 = team
            team2_score += 1
        elif team == team_2:
            team2_score += 1

if team1_score > team2_score:
    print(team_1)
elif team2_score > team1_score:
    print(team_2)