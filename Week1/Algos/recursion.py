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


# fibinocci iterative function that returns an array of fib numbers up to the number you put in 
def fibs(n):
    f = []
    a = 0
    b = 1
    if n == 0 or n == 1:
        print (n)
    else:
        f.append(a)
        f.append(b)
        while len(f) != n:
            temp = a + b
            f.append(temp)
            a = b
            b = temp
    print (f)
fibs(10)

def fib(num):
    

