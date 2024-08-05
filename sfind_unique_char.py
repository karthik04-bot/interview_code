"""
LG SOFT
"""

s = "calculator"

#Medhod-1
from collections import Counter
c=Counter(s)
for char in s:
    if c[char]==1:
        print(char)
        break

#Method-2
for i in range(len(s)):
    found = True
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            found = False
            break
    if found:
        print(s[i])
        break

Method-3
d={}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for k,v in d.items():
    if v == 1:
        print(k)
        break