for i in range(2,10):
	for x in range(2,i):
		if i % x == 0:
			print(f"{i} is multiplication of {x} and {i//x}")
	else:
		print(f"{i} is prime number")
