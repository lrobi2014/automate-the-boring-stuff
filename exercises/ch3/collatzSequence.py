import sys

def collatz(number):
    if (number % 2 == 0):
        return number // 2
    else:
        return  3 * number + 1

# Start of program
print('Enter number:') 
try:
    collatzResult = collatz(int(input())) 
except ValueError:
    print('Error: value entered must be an integer. Enter number:')
    collatzResult = collatz(int(input())) 

while (collatzResult != 1): # Collatz sequence loop
    print(str(collatzResult))
    collatzResult = collatz(collatzResult)

print(collatzResult) # Print final value that should be 1
sys.exit()