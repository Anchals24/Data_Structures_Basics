#def fact(n):
	#smallest subproblem where we know the answer
	#if n == 1:
		#return(1)
	# recursive assumption
	#else:
		#subproblem = fact(n-1)
	#self work
		#return n * subproblem
#print(fact(int(input())))


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
#print(fib(int(input())))

def inc(n):
	if n == 0:
		return
	else:
		inc(n-1)
		print(n)
#inc(7)

def decr(n):
	if n == 0:
		return
	else:
		print(n)
		decr(n-1)
#decr(9)

def incrdecr(n):
	if n == 1: #what if i will put n == 2 here........ create a tree as well.
		print(1)
		return
	else:
		print(n) #self work 1 
		incrdecr(n-1) #Recursive assumption : incrdecr(n-1) ... 1 ...... incrdecr(n-1)
		print(n) #self work 2
#incrdecr(5)

def cou(n):
	#base case
	if n == 1 or n == 2:
		return n+1
	#recursive case
	else:
		subproblem1 = cou(n-1)
		subproblem2 = cou(n-2)
	#self work
		return subproblem1 + subproblem2
#print(cou(0))
