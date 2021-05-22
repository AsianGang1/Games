fin = open('primes.in')
fout = open('primes.out', 'w')
num = int(fin.readline())

for i in range(num - 1, 2, -1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            print(i,j)
            prime = False
    if prime:
        fout.write(str(i))
        break