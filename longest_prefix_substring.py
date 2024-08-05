"""
find longest prefix out of list inside string
"""

Input=["geeksforgeeks","geeks","geek","geezer"]

# Method-1
# def longest_prefix(minimum, lenght):
#     count = 0
#     for i in range(len(Input)):
#         if minimum[:lenght] in Input[i]:
#             count += 1
#     if count != len(minimum):
#         m = len(minimum) - 1
#         longest_prefix(minimum,m)
#     print(minimum[:count])
#     return minimum[:count]
#
# minimum = min(Input)
# print(minimum)
# l = longest_prefix(minimum, len(minimum))
# print("longest prefix inside list is {}".format(l))





