import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

for x in q:
    i = bisect.bisect_left(a, x)
    if i < n and a[i] == x:
        print("YES")
    else:
        print("NO")
