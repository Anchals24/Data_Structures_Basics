#suffix sum
#Method1:

Arr = [10,20,10,5,15]
Arr.reverse()
leng = len(Arr)
suffix_sum = [0 for i in range(leng+1)]
suffix_sum[0] = Arr[0]
for a in range(1 , leng):
    suffix_sum[a] = suffix_sum[a-1] + Arr[a]
print(suffix_sum)

#Method2: (Using slicing concept.)
A = [10 ,20 , 10, 5 , 15]
suffix_sum = []
for i in range(len(A)):
    s = sum(A[ : i +1])
    #print(s)
    suffix_sum.append(s)
print(suffix_sum)