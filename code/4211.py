import re
print(max(map(int, re.findall(r'\d+', input()))))
