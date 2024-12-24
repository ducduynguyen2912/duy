n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

main_diag = sum(a[i][i] for i in range(n))
anti_diag = sum(a[i][n - i - 1] for i in range(n))

print(main_diag)
print(anti_diag)
