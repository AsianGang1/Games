fin = open("grandprix.in")
fout = open("grandprix.out", "a")
n, p = fin.readline().split()
n = int(n)
p = int(p)
powers = fin.readline().split()
double_break = False
for i in powers:
    for j in powers:
        if int(i) + int(j) == p:
            fout.write(str(powers.index(i) +1)+ " " + str(powers.index(j)+1))
            double_break = True
            break
    if double_break:
        break
