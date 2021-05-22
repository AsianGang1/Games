fin = open('gymnastics.in')
fout = open('gymnastics.out', 'w')
k, n = list(map(int, fin.readline().split()))
thingy = []
pairs = 0
for i in range(0, k):
    thingy.append(list(map(int, fin.readline().split())))
first_statements = []
for i in range(0, n):
    for j in range(i + 1, n):
        first_statements.append((thingy[0][i], thingy[0][j]))
for i in range(1, k):
    new_statements = first_statements.copy()
    for j in first_statements:
        index_1 = thingy[i].index(j[0])
        index_2 = thingy[i].index(j[1])
        if index_1 > index_2:
            new_statements.remove(j)
    first_statements = new_statements
fout.write(str(len(first_statements)))
