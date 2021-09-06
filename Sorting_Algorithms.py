#Count_Sort

A = [3 , 5 , 8 , 9, 6 , 2 , 3 , 5 , 5]
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
while c < lc:
    if count[c] == 0:
        c += 1
    else:
        sortedd.append(c)
        count[c] -= 1
print(sortedd)