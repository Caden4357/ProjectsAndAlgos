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
    if num < 2:
        return num
    return fib(num-1) + fib(num-2)
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))

def fibIter(num):
    if num < 2:
        return num
    num1 = 0
    num2 = 1
    for i in range(2, num, 1):
        temp = num1 + num2
        num1 = num2
        num2 = temp
    return num1+num2
print(fibIter(0))
print(fibIter(1))
print(fibIter(2))
print(fibIter(3))
print(fibIter(4))
print(fibIter(5))
print(fibIter(6))
print(fibIter(7))
