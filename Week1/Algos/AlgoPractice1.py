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