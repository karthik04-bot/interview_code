dic = {'a':3, 'b':1, 'c':2}

# Method-1:

# sort=sorted([(v,k) for k,v in dic.items()])
# d=dict((k,v) for v,k in sort)
# print(d)

print({k:v for k,v in sorted(dic.items(),key=lambda k:k[1])})

