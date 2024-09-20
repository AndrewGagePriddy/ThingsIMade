

def Fib(i):
	f1 = 0
	f2 = 1
	f = open("FibonacciSequence.txt","w")
	
	for t in range(i):
			
		#this line of code will write it out vertically
		#txt = f"{f1} \n"
		f.write(str(f1))
		f3 = f1 + f2
		f1 = f2
		f2 = f3
			
			
			
		
	f.close()
