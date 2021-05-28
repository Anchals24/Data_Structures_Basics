#Implemented power function using Recursion........................................

L = [1]
def bin(x, y):
    
    #base case
    if y == 0:
        L.append(1)
        return 1
    elif y == 1:
        L.append(x)
        return x
    #recursive assumption
    else:
        subproblem1 = bin(x , y-1)
    #self work
        L.append(x*subproblem1)
        return x*subproblem1
(bin(2,8))
I = []
str1 = ""
N = int(input())
while N != 0:
    digit = N % 10 
    str1 += str(digit)
    N = N // 10
print(str1)
for s in str1:
    I.append(int(s))
leng = len(I)
summ = 0
for i in range(leng):
    if I[i] == 1:
        summ = summ + L[i]
print(summ) 


#OR 

Powers = []
for x in range(31):
    Powers.append(2**x)
N = int(input())
str1 = ""
while N != 0:
    digit = N % 10
    str1 += str(digit)
    N = N//10
summ = 0
leng = len(str1)
for s in range(leng):
    if int(str1[s]) == 1:
        summ = summ + Powers[s]
print(summ)
