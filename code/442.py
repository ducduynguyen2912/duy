class S:
    def __init__(s, t, p, c):
        s.t, s.p, s.c = t, p, c

    def avg(s):
        return s.c / s.p if s.p > 0 else 0

n = int(input())
a = []
for _ in range(n):
    t, p, c = input(), int(input()), float(input())
    a.append(S(t, p, c))

a.sort(key=lambda x: (x.avg(), x.t))

with open('sach.txt', 'w') as f:
    for s in a:
        f.write(f'{s.t} {s.p} {s.c}\n')
