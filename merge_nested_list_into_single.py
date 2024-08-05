

"""
Merge nested list into single list.

o/p expected = [11, 31, 14, 134, 144, 121, 321, 212, 22, 223, 43]
"""
def a(l, res=[]):
    for i in l:
        if isinstance(i, list):
            a(i, res=res)
        else:
            res.append(i)
    return res

l = [[11, 31], 14, [134, [144, 121], [321], []], 212, [22, 223, 43]]
b = a(l)
print(b)