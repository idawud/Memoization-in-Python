import functools
import timeit

@functools.lru_cache(maxsize=128)
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)
# Benchmark of fibonacci running time:  0.00010129999999999861
# Benchmark of fibonacci running time:  2.299999999996749e-06
# Benchmark of fibonacci running time:  1.7000000000003124e-06

print("Benchmark of fibonacci running time: ", timeit.timeit('fibonacci(35)', globals=globals(), number=1))
print("Benchmark of fibonacci running time: ", timeit.timeit('fibonacci(35)', globals=globals(), number=1))
print("Benchmark of fibonacci running time: ", timeit.timeit('fibonacci(35)', globals=globals(), number=1))