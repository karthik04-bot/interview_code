l=[1,2,3,4,5,6,7,8,9,10]

f=filter(lambda x:x%2==0, l)
print(f.__next__())
# for num in f:
#     print(num, end=" ")


# print(list(f))

# def even_num(num):
#     if num % 2 == 0:
#         print("%s is even num"%(num))
#
# a = filter(even_num, l)

# for i in a:
#     print(i)

