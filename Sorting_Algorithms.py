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


#Radix_Sort
Arr = [23 , 123 , 234 , 1234 , 765 , 9988]
leng = len(Arr)
maxi = max(Arr)
maxidigits = 0
while maxi > 0:
    #digit = maxi % 10
    maxidigits += 1
    maxi = maxi // 10
bins = [0] * 10
for i in range(maxidigits):
    for j in range(leng):
        digits = 0
        while Arr[j] > 0:
            digits += 1
            Arr[j] = Arr[j] // 10

        bins.insert(digits , Arr[j])
    k = 0
    for x in range(10):
        Arr[j] = bins.remove(bins[x])
        k += 1
print(Arr)

#Still need to check it. Raw code.
