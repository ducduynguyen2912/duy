n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

is_upper = all(a[i][j] == 0 for i in range(1, n) for j in range(i))
is_lower = all(a[i][j] == 0 for i in range(n - 1) for j in range(i + 1, n))

if is_upper:
    print("UPPER TRIANGLE")
elif is_lower:
    print("LOWER TRIANGLE")
else:
    print("NONE")
