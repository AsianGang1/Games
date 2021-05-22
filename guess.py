fin = open("guess.in")
fout = open("guess.out", "a")
n = int(fin.readline())
animals = [fin.readline().split() for i in range(0, n)]
for i in animals:
    i[1] = int(i[1])
total_attributes = [item for sublist in animals for item in sublist[2:]]
most = 0
for i in animals:
    others = animals.copy()
    others.remove(i)
    for j in others:
        commons = list(set(j[2:]).intersection(i[2:]))
        print(commons)
        if len(commons) > most:
            most = len(commons)
fout.write(str(most + 1))
