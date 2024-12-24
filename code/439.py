m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

magic_rows = [i + 1 for i in range(m) if sum(a[i]) % 7 == 0]

if magic_rows:
    print(*magic_rows)
else:
    print("NO")
