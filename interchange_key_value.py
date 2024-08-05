dic = {"a":[1,2],"b":[1,3,4],"c":[1,4]}
expected_out = {1: ['a', 'b', 'c'], 2: ['a'], 3: ['b'], 4: ['b', 'c']}

d={}
for k,v in dic.items():
    for values in v:
        if values not in d:
            d[values]=[k]
        else:
            d[values].append(k)
print("final dict {}".format(d))