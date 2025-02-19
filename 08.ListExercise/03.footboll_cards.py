kicked_players = input().split()

a_team_players = 11
b_team_players = 11

for player in kicked_players:
    if player[0] == "A":
        a_team_players -= 1
    elif player[0] == "B":
        b_team_players -= 1
    
    if a_team_players < 7 or b_team_players < 7:
        break

print(f"Team A - {a_team_players}; Team B - {b_team_players}")

if a_team_players < 7 or b_team_players < 7:
    print("Game was terminated")