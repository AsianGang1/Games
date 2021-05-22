fin = open('hps.in')
fout = open('hps.out', 'w')
n = int(fin.readline())
games = []
for i in range(0, n):
    games.append(list(map(int, fin.readline().split())))
print(games)
max_wins = 0
for hoof_number in range(1, 4):
    for scissors_number in range(1, 4):
        wins = 0
        if hoof_number == scissors_number:
            continue
        for game in games:
            # wins when hoof beats scissors
            if game[0] == hoof_number and scissors_number == game[1]:
                wins += 1
            # wins when paper beats hoof
            elif game[0] != hoof_number and game[0] != scissors_number and hoof_number == game[1]:
                wins += 1
            # wins when scissors beats paper
            elif game[0] == scissors_number and game[1] != hoof_number and game[1] != scissors_number:
                wins += 1
        if wins > max_wins:
            max_wins = wins
fout.write(str(max_wins))
