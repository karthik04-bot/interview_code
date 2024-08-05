"""
Find longest possible sub string
"""

st="xyzyzxzxw"
l ={}
s=0
max_len = 0

for i,char in enumerate(st):
    if char in l and l[char] >= s:
        s = l[char] + 1
    else:
        max_len = max(max_len, i-s+1)
print(max_len)



