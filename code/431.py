m, n, k = map(int, input().split())
count = 0
for _ in range(m):
    row = map(int, input().split())
    count += sum(1 for x in row if x == k)
print(count)
