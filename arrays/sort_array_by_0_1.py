array = [1,3,4,1,0,2,21,1]
#o = [0,0,0,3,4,2,3,4,10]

#Method-1
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[j] == 0 or array[i] == 1:
            array[i], array[j] = array[j], array[i]
            print("array", array)

print(array)

# i=0
# j= len(array) - 1
# while i < j:
#     if array[i] != 0:
#         array[i], array[j] = array[j], array[i]














