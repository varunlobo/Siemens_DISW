
"""
@author: varulobo

Siemens coding test for practise

"""

'''
Question 2 b:
    
'''

import numpy as np     #using numpy library to create an array of random integers

arr1= np.random.randint(1,10000000,1000)  #random array 1

arr2= np.random.randint(1,10000000,1000)  #random array 2

import timeit      # importing timeit function to measure time taken to execute this program.

start_time = timeit.default_timer()  #timer start

def smallest_difference(arr1, arr2):
    arr1.sort()      #sorting arrays
    arr2.sort()      #sorting arrays
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



x,y,z=(smallest_difference(arr1, arr2))

print("The number in the 1st array is:" + str(x))
print("The number in the 2nd array is:" + str(y))
print("The smallest difference is:" + str(z))

end_time = timeit.default_timer()  # timer ends

elapsed_time = end_time - start_time  # difference gives time taken for execution

print("Time taken: ", elapsed_time)

'''
The complexity of the while loop is O(n) while that of sort() function is O(nlogn)
Total algorithm complexity is O(n) + O(nlogn) = O(nlog n))

'''
