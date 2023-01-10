"""
@author: varulobo

Siemens coding test for practise

"""

''' Question # 1 b:
Provide 2 or 3 different ways to calculate the pair of values (one value in each array) with the smallest non-negative difference.

Return the elements in the array and the smallest non-negative difference.'''




def smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i=0              #initialization of index to 0
    j=0              #initialization of index to 0  
    min_diff=10**200 #an arbirary large number
    a=0              #to store value from 1st array
    b=0              #to store value from 2st array
    
    while i < len(arr1) and j < len(arr2):
        if abs(arr1[i] - arr2[j]) < min_diff:
            min_diff = abs(arr1[i] - arr2[j])
            a, b = arr1[i], arr2[j]
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return (a, b, min_diff)

arr1 = [47,24,95,184,13,3,12,18]
arr2 = [83,9,32,29,52,90,108,14]

x,y,z=(smallest_difference(arr1, arr2))

print("The number in the 1st array is:" + str(x))
print("The number in the 2nd array is:" + str(y))
print("The smallest difference is:" + str(z))




