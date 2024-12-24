import re
s = input()
n = sorted(map(int, re.findall(r'\d+', s)))
i = 0
for x in re.split(r'(\d+)', s):
    print(x if not x.isdigit() else str(n[i]) if i < len(n) else '', end='')
    if x.isdigit(): i += 1
