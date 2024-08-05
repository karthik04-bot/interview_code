"""
1.Find number of duplicate elements on same array and between the array
2.FInd the positions(index) of duplicated elements
3.Find the number of occurance of duplicated elements between the array
"""


string1 = "AAA BBB XXX LLL KKKK IIII"
string2 = "AAA JJJ PPP BBB XXX HHHHH PPP"

def duplicate_elements(arr1, arr2=None, pos = None):
    l=[]
    print(arr2)
    if arr2:
       arr1.extend(arr2)
    arr = len(arr1)

    for i in range(arr):
        found = False
        if arr1[i] not in l:
            l.append(arr1[i])
        else:
            found = True
            print("Duplicate elements in array is {}".format(arr1[i]))
            if pos:
                p = []
                print("Duplicate elements positions {} is {}".format(arr1[i], i))

    if not found:
        print("Duplicate elements are not found in the array {}".format(l))


string1 = string1.split()
string2 = string2.split()

#Duplicate elements on same array1
duplicate_elements(string1)
#Duplicate elemets on same array2
duplicate_elements(string2)
#Duplicate elements between the array1 and array2
duplicate_elements(string1, string2)
#Duplicate elements positions
duplicate_elements(string1, string2, True)
#Number of duplicate elements present

