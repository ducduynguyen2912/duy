s = input()
r = {}
for c in s:
    r[c] = r.get(c, 0) + 1
for k, v in r.items():
    print(f"'{k}': {v}", end=', ')
