score1 = 0
score2 = 0

with open('input.txt', 'r') as f:
    while line := f.readline():
        opponent, me = line.strip().split(' ')
        opp_val = ord(opponent) - ord('A') + 1
        me_val = ord(me) - ord('X') + 1

        game_score = me_val
        if me_val == (opp_val % 3) + 1:
            game_score += 6
        elif me_val == opp_val:
            game_score += 3
        score1 += game_score

with open('input.txt', 'r') as f:
    while line := f.readline():
        opponent, goal = line.strip().split(' ')
        opp_val = ord(opponent) - ord('A') + 1

        if goal == 'X':
            me_val = (opp_val - 2) % 3 + 1
            game_score = 0
        elif goal == 'Y':
            me_val = opp_val
            game_score = 3
        else:
            me_val = (opp_val % 3) + 1
            game_score = 6

        game_score += me_val
        score2 += game_score

print(f'(1) Final score following guide: {score1}')
print(f'(2) Final score correct strat: {score2}')
