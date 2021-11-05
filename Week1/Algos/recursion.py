# factorial recursive function 
from time import time
from time import perf_counter
from timeit import default_timer as timer

# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1)) 
start = perf_counter()
print(factorial(6))
end = perf_counter()
print(end-start)

# Iterative factorial function

def iterFactorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact
start = perf_counter()
print(iterFactorial(6))
end = perf_counter()
print(end-start)



