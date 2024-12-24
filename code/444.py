n = int(input())
e, m = None, float('inf')
for _ in range(n):
    i, t, s, a = input().split()
    s, a = float(s), int(a)
    l = s * 2000000 + a
    if l < m:
        e, m = (i, t, s, a, l), l
print("Nhan vien co luong thap nhat")
print(*e)
