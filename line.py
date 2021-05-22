fin = open("line.in")
fout = open("line.out", "a")
n, k = fin.readline().split()
n = int(n)
k = int(k)
horses = fin.readline().split()
for i in range(0, n):
    if int(horses[i])<k<int(horses[i+1]):
        fout.write(str(i+1))