
"""
@author: varulobo

Siemens coding test for practise

"""

''' Question 1 a:
Provide 2 or 3 different ways to calculate the pair of values (one value in each array) with the smallest non-negative difference.

Return the elements in the array and the smallest non-negative difference.'''



def func(arr1, arr2):
    
    lowest_num = []
    
    for i in arr1:
        
        for j in arr2:
            
            lowest_num.append(abs(i-j))
            
    return min(lowest_num)
        
arr1 = [47,24,95,184,13,3,12,18]
arr2 = [83,9,32,29,52,90,108,14]
    
L=func(arr1,arr2)

for i in range(0,len(arr1),1):
    
    for j in range(0,len(arr2),1):
        
        
        if abs(arr1[i] - arr2[j])==L:
            
            print("The number in the 1st array is:" + str(arr1[i]))
            print("The number in the 2nd array is:" + str(arr2[j]))
            print("The smallest difference is:" + str(L))
            break
 
        
