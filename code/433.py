m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

n, p = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

c = [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(p)] for i in range(m)]

for row in c:
    print(*row)
