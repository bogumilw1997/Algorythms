
# The function that randomizes the order of the list is kept in the
# "random" module, so we need to import that here.
import random
# The sys.argv list gives us the command line arguments to the
# script. To use it, we also need to import the "sys" module.
import sys
# Here's where we import the load_numbers function from above.

# And here, we pass the first command line argument (which should be
# the path to a file) to load_numbers, and store the returned list of
# numbers in a variable.
numbers = [8,2,5,6,1, 3, 2, 3]

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index+1]:
            return False
        
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts +=1
    
    return values

print(numbers)
print(bogo_sort(numbers))