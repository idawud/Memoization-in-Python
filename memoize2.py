import timeit
cache = {}
def fibonacci(n):
	global cache
	if n in cache:
		return cache[n]
	else: 
		if n == 0:
			cache[n] = 0
			return 0
		elif n == 1:
			cache[n] = 1
			return 1
		else:
			cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
			return cache[n]

# Benchmark of fibonacci running time:  6.699999999999762e-05
# Benchmark of fibonacci running time:  2.3999999999996247e-06
# Benchmark of fibonacci running time:  2.2000000000008124e-06
# print(fibonacci(35))
print("Benchmark of fibonacci running time: ", timeit.timeit('fibonacci(35)', globals=globals(), number=1))
print("Benchmark of fibonacci running time: ", timeit.timeit('fibonacci(35)', globals=globals(), number=1))
print("Benchmark of fibonacci running time: ", timeit.timeit('fibonacci(35)', globals=globals(), number=1))