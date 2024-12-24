n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

is_symmetric = True
for i in range(n):
    for j in range(i):
        if a[i][j] != a[j][i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

print("YES" if is_symmetric else "NO")
