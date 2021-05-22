fin = open('herding.in')
fout = open('herding.out', 'w')
locations = list(map(int, fin.readline().split()))
if locations[0]+1 == locations[1] and locations[1] + 1 == locations[2]:
    fout.write("0\n")
elif locations[1] - locations[0] == 2 or locations[2] - locations[1] == 2:
    fout.write("1\n")
else:
    fout.write("2\n")
fout.write(str(max(locations[2] - locations[1], locations[1] - locations[0]) - 1))
