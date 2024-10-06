# Python3 program to find 
# if a number is Surd or not.

# define a isSurd function which
# Returns true if x is Surd number.
def isSurd(n) :
	
	i = 2
	for i in range(2, (i * i) + 1) :
		
		# Try all powers of i
		j = i
		while (j < n) :
			j = j * i

		if (j == n) :
			return False
	
	return True

# Driver code
if __name__ == "__main__" :
	
	n = 15
	
	if (isSurd(n)) :
		print("Yes")
		
	else :
		print("No")

# This code is contributed 
# by Ankit Rai1
