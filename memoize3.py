import timeit

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)


def memoize(func):
	cache = dict()
	def memoized_func(*args):
		if args in cache:
			return cache[args]
		result = func(*args)
		cache[args] = result
		return result
	
	return memoized_func

memoized_fibonacci = memoize(fibonacci)

# Benchmark of fibonacci running time:  15.2866316
# Benchmark of fibonacci running time:  3.1000000006997652e-06
# Benchmark of fibonacci running time:  2.3999999996249244e-06

print("Benchmark of fibonacci running time: ", timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1))
print("Benchmark of fibonacci running time: ", timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1))
print("Benchmark of fibonacci running time: ", timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1)) 