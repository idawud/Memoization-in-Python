import timeit
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)

# average time taken is 15sec
#print(fibonacci(35))
print("Benchmark of fibonacci running time: ", timeit.timeit('fibonacci(35)', globals=globals(), number=1))