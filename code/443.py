class S:
    def __init__(s, t, p, c):
        s.t, s.p, s.c = t, p, c

with open('sach.txt', 'r') as f:
    a = []
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        t, p, c = lines[i].strip(), int(lines[i+1].strip()), float(lines[i+2].strip())
        a.append(S(t, p, c))

r = [s for s in a if s.c > 100000 and s.p < 200]

with open('ketqua.txt', 'w') as f:
    for s in r:
        f.write(f'{s.t} {s.p} {s.c}\n')
