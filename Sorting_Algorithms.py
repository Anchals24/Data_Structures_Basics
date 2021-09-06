#Count_Sort


A = [3 , 5 , 8 , 9, 6 , 2 , 3 , 5 , 5]
print("Unsorted Array is >> " , A)
leng = len(A)
maxi = max(A)
count = []
sortedd = []
for i in range(maxi+1):
    count.append(0)
for i in A:
    count[i] += 1
lc = len(count)
c = 0
j = 0
while c < lc:
    if count[c] == 0:
        c += 1
    else:
        A[j] = c
        j += 1
        count[c] -= 1
print("Sorted Array is >>" , A)
