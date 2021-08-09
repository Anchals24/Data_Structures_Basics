#Prefix_Sum or Cumulative sum of an array
#Method 1: 
Arr = [5, -2, 3 , 1, 2]
leng = len(Arr)
prefix_sum = [0 for i in range(leng+1)]
prefix_sum[0] = Arr[0]
for a in range(1 , leng):
    prefix_sum[a] = prefix_sum[a-1] + Arr[a]
print(prefix_sum)

#Method 2: Using slicing concept.

A = [10 ,20 , 10, 5 , 15]
C_A = []
for i in range(len(A)):
    s = sum(A[ : i +1])
    #print(s)
    C_A.append(s)
print(C_A)

