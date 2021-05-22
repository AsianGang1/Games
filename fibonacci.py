fin = open("fibonacci.in")
fout = open("fibonacci.out", "w")
n = int(fin.readline())


def get_num(n):
    prev2_num = 1
    prev_num = 0
    nth_term = 0
    for x in range(0, n):
        nth_term = prev_num + prev2_num
        prev2_num = prev_num
        prev_num = nth_term
    fout.write(str(nth_term))


get_num(n)
