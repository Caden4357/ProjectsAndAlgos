# Set myNumber to 42. Set myName to your name. Now swap myNumber into myName & vice versa.
from re import I


def swap():
    myNumber = 42
    myName = "Caden"
    temp = myNumber
    myNumber = myName
    myName = temp
    print(f'My name is {myName}')
    return(f'My number is {myNumber}')
print(swap())

# Print integers from -52 to 1066 using a FOR loop.

def printNumbers():
    for i in range(-52, 1067, 1):
        print(i)
printNumbers()

# Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.
def beCheerful():
    print('Good Morning ' * 98)
beCheerful()

# Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.
def multiplesOfThree():
    for i in range(-300, 1, 1):
        if(i == -3 or i == -6):
            continue
        else:
            print(i)
multiplesOfThree()

# Print integers from 2000 to 5280, using a WHILE.
def printWithWhileLoop():
    i = 2000
    while i <= 5280:
        print (i)
        i += 1
printWithWhileLoop()

# If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day...." 
def birthday(num1, num2):
    birthdayNum1 = 9
    birthdayNum2 = 19
    if(num1 == birthdayNum1 or num1 == birthdayNum2 & num2 == birthdayNum2 or num2 == birthdayNum1):
        print("Happy birthday")
    else:
        print("Just another day")

birthday(6,10)
birthday(9,19)

#Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.


# Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.

def multiplesOfFive():
    count = 0
    for i in range(512, 4097, 1):
        if(i % 5 == 0):
            count += 1
            print(i)
    return count
print(multiplesOfFive())

# Print multiples of 6 up to 60,000, using a WHILE.
def multiplesOfSix():
    i = 6
    while(i <= 60000):
        if(i % 6 == 0):
            print(i)
            i+=1
        else:
            i+=1
multiplesOfSix()

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
def countingDojo():
    for i in range(101):
        if(i % 10 == 0):
            print("Dojo")
        elif(i % 5 ==0):
            print("Coding")
        else:
            print(i)
countingDojo()
    
# Your function will be given an input parameter incoming. Please console.log this value.
def printValue(incoming):
    print(incoming)
printValue("this is a string")
printValue(26)
printValue([6,5,9,8,6,666])

def bigSum():
    sum = 0
    for i in range (1, 300000, 2):
        sum += i
    return sum
print(bigSum())

# Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.
def countdownByFour():
    num = 2016
    while num > 0:
        print(num)
        num -= 4
countdownByFour()

# Based on earlier “Countdown by Fours”, given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).
    # lowNum=2
    # highNum=9
    # mult=3 
    # Im gonna use another variable called count if lowNum is higher then mult I know to start count at 2 atleast then I will compare it to lowNum if lowNum is still higher I will repeat that process once mult is higher than lowNum I will continue multiplying it and comparing it to high num 
def flexibleCountdown(lowNum, highNum, mult):
    for i in range(1,highNum,1):
        if(mult * i > highNum):
            break
        if (mult * i < lowNum):
            continue
        elif(mult * i >= lowNum):
            print(mult * i)
flexibleCountdown(5,100,4)


# This is based on “Flexible Countdown”. The parameter names are not as helpful, but the problem is essentially identical; don’t be thrown off! Given 4 parameters (param1,param2,param3,param4), print the multiples of param1, starting at param2 and extending to param3. One exception: if a multiple is equal to param4, then skip (don’t print) it. Do this using a WHILE. Given (3,5,17,9), print 6,12,15 (which are all of the multiples of 3 between 5 and 17, and excluding the value 9).
# given 4 numbers first print the multiples of the first number starting at the second number and stoping at the third number just like above only this time compare the current multiple to the 4th number if it is the multiple is the same as the current num dont print it 

def finalCountdown(lowNum, highNum, mult, xNum):
    for i in range(1,highNum,1):
        if(mult * i > highNum):
            break
        if (mult * i < lowNum):
            continue
        if(mult * i >= lowNum and mult * i != xNum):
            print(mult * i)
finalCountdown(5,17,3,9)
