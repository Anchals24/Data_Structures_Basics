#Recusrion Part1 : Very basic Problems. [Beginner Level]
#Recursion is a process in which a function calls itself directly or indirectly and the corresponding function is called as recursive function.

#Program1 : Finding factorial of a number...
""" 5! = 5 * 4 * 3 * 2 * 1 """

def fact(n):
	#smallest subproblem where we know the answer or the base case
	if n == 1:
		#return(1)
	#recursive assumption
	else:
		subproblem = fact(n-1)
	#self work
		return n * subproblem
print(fact(int(input())))

#Fibonacci of a number...
""" 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …… """

def fib(n):
	#base case
	if (n == 0 or n == 1):
		return n
	#recursive assumption
	else:
		subproblem1 = fib(n-1)
		subproblem2 = fib(n-2)
	#self work
		return subproblem1 + subproblem2
print(fib(int(input())))

#Printing the numbers in incrementing order... 
""" 0 , 1, 2 , 3..... """
def inc(n):
	if n == 0:
		return
	else:
		inc(n-1)
		print(n)
inc(7)

#Printing the numbers in decrementing order... 

def decr(n):
	if n == 0:
		return
	else:
		print(n)
		decr(n-1)
decr(9)

#printing elements in decreasing  and increasing order
""" 3 2 1 2 3"""
def decrincr(n):
	if n == 1: #what if i will put n == 2 here........ create a tree as well.
		print(1)
		return
	else:
		print(n) #self work 1 
		decrincr(n-1) #Recursive assumption : decrincr(n-1) ... 1 ...... decrincr(n-1)
		print(n) #self work 2
decrincr(5)



