fin = open('NNN.in')
fout = open('NNN.out', 'w')
n, k = map(int, fin.readline().split())
line = fin.readline()
in_row_full = True
for i in range(0, n):
    in_row = True
    for j in range(i+1, i+k):
        if j > n-1:
            in_row = False
            break
        if line[j] != line[i]:
            in_row = False
    if in_row:
        fout.write("false")
        in_row_full = False
        break
if in_row_full:
    fout.write("true")
