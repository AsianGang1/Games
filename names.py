fin = open("names.in")
fout = open("names.out", "w")
temp = fin.readline().split()
n = int(temp[0])
g = int(temp[1])
names_n = fin.readline().split()
names_g = fin.readline().split()
shared = []
for name in names_n:
    for name_2 in names_g:
        if name_2 == name:
            shared.append(name_2)
            break
unique = []
if shared:
    for name in shared:
        if name not in unique:
            unique.append(name)
    fout.write(" ".join(sorted(unique)))
else:
    fout.write("-1")
