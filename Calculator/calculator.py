import time


def main():
    # take input from user
    dda = input('please enter an operation. (add, sub, mult, div, per, exp, exit):\t')
    num1 = float(input('please enter a number:\t'))
    num2 = float(input('please enter another number:\t'))
    # pass input to mode
    print("The answer is:")
    print(mode(dda, num1, num2))
    
    return 0

def mode(function, x, y): 
    if function == 'add':
        return add(x, y)
    elif function == 'exp':
        return exponent(x,y)
    elif function == 'exit':
        exit(0)
   # add code for testing what function should be called
    return #answer

def add(x, y):
    # add functionality for adding
    return x+y

def  subtract(x, y):
    # add code here
    
    return x-y

def multiply(x, y):
    # add code here
    return #answer

def divide(x, y):
    # add code here
    if y == 0:
       print("Error: can not divide by 0")  
       return
    return x/y

def percent(x):
    # percent functionality for adding
    return x/100
    
def exponent(x,y):
    number = 1
    for pool in range(0, int(y)):
        number = x * number
    return number
    
if __name__ == "__main__":
    main()