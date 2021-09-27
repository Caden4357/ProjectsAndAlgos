# Set myNumber to 42. Set myName to your name. Now swap myNumber into myName & vice versa.
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
