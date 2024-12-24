m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

total = sum(sum(row) for row in a)
avg = total / (m * n)

print(f"{avg:.2f}")

for i in range(m):
    for j in range(n):
        if a[i][j] > avg:
            print(a[i][j], i + 1, j + 1)
