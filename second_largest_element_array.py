l=[2,200,100,35,40,150,400,600,600,4000,600,600,700,700]

"""
#Method 1 - Fibonasi serious
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print("second largest element is {}".format(l[-2]))
"""
#Method-2

# largest=second=l[0]
# for i in range(len(l)):
#     if l[i] > largest:
#         second = largest
#         largest = l[i]
#     elif l[i] > second and l[i] != largest:
#         second = l[i]
# print("Second largest element is {}".format(second))

lr = [10,2,3,4,100,3,5,6,9,50,40]

l=s=lr[0]
for i in lr:
    if i > l:
        s = l
        l = i
    if i > s and i != l:
        s = i
print(s)
