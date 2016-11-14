def prime(n):

	if type(n) == int and n > 1:
		for num in range(2,n):
			if (n % num) == 0:
				return False
	return True

print prime(3)
