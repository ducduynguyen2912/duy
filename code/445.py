n = int(input())
a = []
for _ in range(n):
    t, i, s, p = input().split()
    s, p = float(s), int(p)
    l = s * 2000000 + p
    a.append((i, t, s, p, l))
a.sort(key=lambda x: -x[4])
print(f"Danh sach nhan vien da sap xep: {n}")
for e in a:
    print(*e)
