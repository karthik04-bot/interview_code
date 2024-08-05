nums = [2,20,4,10,3,4,5]
# l=[]
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + 1 == nums[j] and nums[i] not in l and nums[j] not in l:
#             l.append(nums[i])
#             l.append(nums[j])
# print(l)

s = set(nums)
longest = 0

for n in s:
    if (n-1) not in s:
        lenght = 0
        while (n+lenght) in s:
            lenght+= 1
        longest = max(longest, lenght)
print(longest)
