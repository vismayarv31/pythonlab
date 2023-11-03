def power(base,exponent):
	if exponent==0:
		return 1
	elif exponent==1:
		return base
	else:
		return power(base,exponent-1)*base
base=int(input("enter the number:"))	
exponent=int(input("enter the exponent:"))	
print (power(base,exponent))
