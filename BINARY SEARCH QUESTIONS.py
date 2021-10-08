"""BINARY SEARCH"""
#basic pre-requisite to perform binary search: array must be in  sorted order
#Binary search is all about :
# Finding the mid position 
# and then "deciding" which pointer is needed to be shifted. (in left or right direction)


#Implementing normal binary search in a sorted array:

#We have to search an element in an array and return it's position(index) if it's present else return -1.
#Steps involved:
"""
>> We know the array is already sorted.
>> Hence, we will first take two pointers(var) to track the initial and last element of the array. 
>> These pointers will be storing the first and last index of an array.
>> now we will calculate the mid position. 
>> we will check if the element we are looking for is equal to the mid position element. if they are equal simply return the index.
>> else if it's not equal. there are 2 possible cases only : the number we are searching for is greater or lesser than the element at the mid position.
>> if the mid pos ele is greater than the target number then it's definitely on the left side. Hence we will shift our right pointer towards left portion by setting it as mid-1.
>> else we will shift our left pointer towards the right portion of the array.
>> below is the code for the normal binary search.
"""

def Binary_Search(Arr , data):
    start = 0
    end = len(Arr) - 1
    while start <= end:
        mid = start + (end-start) // 2
        if Arr[mid] == data:
            return mid
        elif Arr[mid] > data:
            end = mid -1
        elif Arr[mid] < data:
            start = mid + 1
    return -1
print(Binary_Search([1,2,3,4,5,6] , 1))

#Finding first occurence of any number:
"""
In this , we need to find the first time a number occurs in an array.
for ex : if an array contains an element thrice, then we need the return the mininum element of these duplicates.
[1 ,2 , 3, 3, 3, 5, 8] if we need to find the first occurence of 3 : it will be 2.
"""
def first_occur(Arr , ele):
    end = len(Arr) - 1
    start = 0
    occur = -1
    while start <= end:
        mid = start + (end-start) // 2
        if Arr[mid] == ele:
            occur = mid
            end = mid-1
        elif Arr[mid] < ele:
            start = mid + 1
        elif Arr[mid] > ele:
            end = mid - 1
    return occur
print(first_occur([2,3,7,7,7,9,8,27] , 35))

#finding last occurence of any number:

"""
In this , we need to find the last time a number occurs in an array.
for ex : if an array contains an element thrice, then we need the return the maximum element of these duplicates.
[1 ,2 , 3, 3, 3, 5, 8] if we need to find the first occurence of 3 : it will be 4.
and the number which is no duplicate? ex : 8 : it's last occurence will be 6.
"""

def last_occur(Arr , ele):
    start = 0
    end = len(Arr) - 1
    l_occur = -1
    while start <= end:
        mid = start + (end - start) // 2
        if Arr[mid] == ele:
            l_occur = mid
            start = mid +1
        elif Arr[mid] > ele:
            end = mid - 1
        elif Arr[mid] < ele:
            start = mid + 1
    return l_occur
print(last_occur([2,3,7,7,7,9,8,27] , 35))
         
#to find the count of an element or number of times an element is repeating

"""
#Find the first occurence by calling the first_occur () and store in a var 
#find the last occurence by calling the last_occur() and store in a var 

ans = (last_occur() - first_occur()) + 1
"""


#Finding the start index of FIRST postive number in a sorted array: 
"""
Let Arr be an array of n distinct integers. Suppose Arr has the following property : 
there exists an index 1 <= k <= n such that A[1]... A[k] is an increasing sequence and A[k+1]......A[n] is a decreasing sequence.
Find k.

We will simply track the first element greater than 0.
"""
def firstpositiveindex(Arr):
    start = 0
    end = len(Arr) - 1
    posindex = -1
    while start <= end:
        mid = start + (end-start) // 2
        if Arr[mid] >= 0:
            posindex = mid
            end = mid -1 
        elif Arr[mid] < 0:
            start = mid+1
    return posindex
ans = firstpositiveindex([-12,-10,-7,-5,-2,8 ,6 , 5 , 4, 3])
print(ans)


#Implementing lower bound function..!!!

"""
lowerbound function: It simply returns the index of the element we have searched or index of the next greater element than it, if the element is not present.
and if the greater ele is also not present return -1.

for ex: [1,2,3,4,5,5,6,7]
ans = 4 [index of the first "5"]
"""

def lower_bound(Arr , num):
    start = 0
    end = len(Arr) - 1
    nextindex = -1
    while start <= end:
        mid = start + (end - start) // 2
        if Arr[mid] < num:
            start = mid + 1
        elif Arr[mid] >= num:
            nextindex = mid
            end = mid - 1
    return nextindex
print(lower_bound([1,2,3,4,6,8,9,10] , 1))

#Implementing upper bound function..!!!
"""
upperbound function: It simply returns the next larger element than the element we have searched.
and if the greater ele is also not present return -1. 
Also, in upper bound if the number we are looking for is also present, it won't return the index of that number but will return the index of next greater element than the searched number.

For ex: 
[3,4,5,6,7,8] , num = 5
ans : 4 [index of 6 cz 6 is greater than 5.]

"""

def upper_bound(Arr , num):
    start = 0
    end = len(Arr) - 1
    nextindex = -1
    while start <= end:
        mid = start + (end - start) // 2
        if Arr[mid] <= num:
            start = mid + 1
        elif Arr[mid] > num:
            nextindex = mid
            end = mid - 1
    return nextindex
print(upper_bound([1,2,3,4,5,5,5,6,8,9,10] , 5))

#How many times a sorted array is sorted
#when array is rotated by shifting elements to the left
def rotations_count(Arr):
    start = 0
    end = len(Arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if Arr[mid] < Arr[mid-1] and Arr[mid] < Arr[mid+1]:
            return mid
        elif Arr[mid] >= Arr[0]:
            start = mid + 1
        elif Arr[mid] <= Arr[-1]:
            end = mid - 1
A = [8,11,12,15,18,2,5,6]
rotations = rotations_count(A)
ans = len(A) - rotations
print(ans)

#when array is rotated by shifting elements towards the right
def rotations_count(Arr):
    start = 0
    end = len(Arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if Arr[mid] < Arr[mid-1] and Arr[mid] < Arr[mid+1]:
            return mid
        elif Arr[mid] >= Arr[0]:
            start = mid + 1
        elif Arr[mid] <= Arr[-1]:
            end = mid - 1
A = [11,12,15,18,2,5,6,8]
print(rotations_count(A))


#Searching for an element in a rotated array!
def Binary_search(Arr , start , end, ele):
    while start <= end:
        mid = start + (end - start) // 2
        if Arr[mid] == ele:
            return mid
        elif Arr[mid] > ele:
            end = mid - 1
        elif Arr[mid] < ele:
            start = mid + 1
    return -1

def rotations_count(Arr): #assuming array has been rotated by shifting towards right
    start = 0
    end = len(Arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if Arr[mid] < Arr[mid-1] and Arr[mid] < Arr[mid+1]:
            return mid
        elif Arr[mid] >= Arr[0]:
            start = mid + 1
        elif Arr[mid] <= Arr[-1]:
            end = mid - 1

def search_rotated(A , ele):
    min_index = rotations_count(A)
    if A[min_index] == ele:
        return min_index
    elif ele >= A[0]:
        return Binary_search(A , 0 , min_index-1 , ele)
    elif ele <= A[0]:
        return Binary_search(A , min_index , len(A)-1 , ele)
        
ans = search_rotated([11,12,15,18,2,5,6,8] , 11)
print(ans)


#Finding floor of an element.

def floor_val(Arr , ele):
    start = 0
    end = len(Arr) - 1
    floor = -1
    while start <= end:
        mid = start + (end-start) // 2
        if Arr[mid] == ele:
            return mid
        elif Arr[mid] > ele:
            end = mid - 1
        elif Arr[mid] < ele:
            start = mid + 1
            floor = mid
    return floor
print(floor_val([1,2,3,4,8,10,10,12,19] , 29))

#Finding ceil of an element.

def ceil_val(Arr , ele):
    start = 0
    end = len(Arr) - 1
    ceil = -1
    while start <= end:
        mid = start + (end-start) // 2
        if Arr[mid] == ele:
            return mid
        elif Arr[mid] > ele:
            end = mid - 1
            ceil = mid
        elif Arr[mid] < ele:
            start = mid + 1
            
    return ceil
print(ceil_val([1,2,3,4,8,10,10,12,19] , 5))
