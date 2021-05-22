import math

n = int(input())
ids = list(map(int, input().split(' ')))
# n = 7
# ids = [11, 2, 17, 13, 1, 15, 3]
# # ids = [1, 3, 5, 7, 9, 11, 13]
eo = []
odds = evens = 0
for i in ids:
    if i % 2 == 0:
        eo.append('e')
        evens += 1
    else:
        eo.append('o')
        odds += 1
new_odds = odds + evens * 2
new_evens = odds * 2 + evens
if evens > odds:
    if new_evens % 3 == 0 or new_evens % 3 == 2:
        print(int(2 * math.floor(new_evens / 3) + (new_evens % 3) / 2))
    else:
        print(int(2 * math.floor(new_evens / 5) + (new_evens % 5) / 2))
else:
    if new_odds % 3 == 0 or new_odds % 3 == 2:
        print(int(2 * math.floor(new_odds / 3) + (new_odds % 3) / 2))
    else:
        print(int(2 * math.floor(new_odds / 5) + (new_odds % 5) / 2))
