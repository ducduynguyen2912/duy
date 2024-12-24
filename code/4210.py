n,q=map(int,input().split())
s=input()
for _ in range(q):
    l,r,c=map(int, input().split())
    print(s[l-1:r].count(c))
