
#Output: [[2, 3, 8, 10],[2, 4, 7, 10],[3, 4, 7, 9],[2, 4, 8, 9],[2, 5, 7, 9],[3, 5, 7, 8]]

"""
Brute Force Logic
"""
# nest_l=[]
# for i in range(len(Input)):
#     for j in range(i+1, len(Input)):
#         for k in range(j+1, len(Input)):
#             for m in range(k+1, len(Input)):
#                 if Input[i]+Input[j]+Input[k]+Input[m] == target:
#                     l=[]
#                     l.append(Input[i])
#                     l.append(Input[j])
#                     l.append(Input[k])
#                     l.append(Input[m])
#                     nest_l.append(l)
# print("Combination of 4 sum elements is {}".format(nest_l))

"""
Optimized code
"""
Input=[10, 2, 3, 4, 5, 9, 7, 8]
target = 23

s=set()
Input.sort()
for i in range(len(Input)):
    for j in range(i+1,len(Input)):
        k=j+1
        m=len(Input)-1
        while k < m:
            sum = Input[i] + Input[j] + Input[k] + Input[m]
            if sum == target:
                s.add((Input[i],Input[j],Input[k],Input[m]))
                k+=1
                m-=1
            elif sum < target:
                k+=1
            elif sum > target:
                m-=1
print("Combinations of all four elements which is equal to traget is {}".format(s))


# nest_l=[]
# sum=0
# for i in range(len(Input)):
#     j=i+1
#     k=len(Input)-1
#     while j < k:
#         print(Input[i],Input[j], Input[k])
#         sum = Input[i] + Input[j] + Input[k]
#         print(i,sum)
#         print(j,k)
#         diff = target - sum
#         print(diff)
#         # print(Input[j+1:k])
#         m = j+1
#         p = k
#         print(i,Input[m:p])
#         if diff in Input[m:p]:
#             if sum + diff == target:
#                 l=[]
#                 l.append(Input[i])
#                 l.append(Input[j])
#                 l.append(Input[k])
#                 l.append(diff)
#                 nest_l.append(l)
#                 j += 1
#                 # k -= 1
#         else:
#             k-=1
#
# res = list(set(tuple(sorted(sub)) for sub in nest_l))
# print("Combination of 4 sum elements is {}".format(res))
#
#
# def combination_sum(nums, target):
#     # Sort nums to handle duplicates and to easily skip unnecessary elements
#     nums.sort()
#     result = []
#
#     def backtrack(start, target, path):
#         if target == 0:
#             result.append(path)
#             return
#         if target < 0:
#             return
#
#         for i in range(start, len(nums)):
#             # Skip duplicates to avoid duplicate combinations
#             if i > start and nums[i] == nums[i - 1]:
#                 continue
#             backtrack(i + 1, target - nums[i], path + [nums[i]])
#
#     backtrack(0, target, [])
#     return result
#
#
# # Example usage:
# nums = [10, 2, 3, 4, 5, 9, 7, 8]
# target = 23
# print(combination_sum(nums, target))




