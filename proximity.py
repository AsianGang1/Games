fin = open('proximity.in')
fout = open('proximity.out', 'w')
n, k = map(int, fin.readline().split())
line = [int(fin.readline()) for cow in range(0, n)]
max_id = 0
for i in range(0, n):
    for j in range(i+1, i+k+1):
        if j > n-1:
            continue
        if line[j] == line[i]:
            max_id = max(max_id, line[i])
fout.write(str(max_id))
