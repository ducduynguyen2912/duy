s = input()
print(", ".join(x for x in s.split(",") if int(x) % 2 != 0))
