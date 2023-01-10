
"""
@author: varulobo

Siemens coding test for practise

"""

'''
Question 2 a:
    
'''

import numpy as np

arr1= np.random.randint(1,10000000,1000)    # using numpy library to create an array of random integers

arr2= np.random.randint(1,10000000,1000)    # using numpy library to create an array of random integers


import timeit                               # importing timeit function to measure time taken to execute this program.

start_time = timeit.default_timer()

def func(arr1, arr2):
    
    lowest_num = []
    
    for i in arr1:                          # outer forloop
        
        for j in arr2:                      # inner for loop
            
            lowest_num.append(abs(i-j))
            
    return min(lowest_num)
        
    
L=func(arr1,arr2)

for i in range(0,len(arr1),1):
    
    for j in range(0,len(arr2),1):
        
        
        if abs(arr1[i] - arr2[j])==L:
            
            print("The number in the 1st array is:" + str(arr1[i]))
            print("The number in the 2nd array is:" + str(arr2[j]))
            print("The smallest difference is:" + str(L))
            break
 
        

end_time = timeit.default_timer()

elapsed_time = end_time - start_time       # timer ends

print("Time taken: ", elapsed_time)        # difference gives time taken for execution

"""
  The complexity of this program is O(n^2) because of the nested FOR loops. 
  The outer loop takes O(n) time and the inner loop takes O(n) time, so their 
  composition is O(n) * O(n) = O(n^2). 

"""