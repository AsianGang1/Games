fin = open("mixmilk.in")
fout = open("mixmilk.out", "a")
capacity = []
fills = []
for i in range(0, 3):
    line = list(map(int, fin.readline().split()))
    capacity.append(line[0])
    fills.append(line[1])
for i in range(0, 100):
    current = i % 3
    next = (i + 1) % 3
    print(fills)
    if fills[current] + fills[next] > capacity[next]:
        fills[current] -= capacity[next] - fills[next]
        fills[next] = capacity[next]
    else:
        fills[next] += fills[current]
        fills[current] = 0
for i in range(0, 3):
    fout.write(str(fills[i])+"\n")
