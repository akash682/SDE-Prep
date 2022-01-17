"""
Algorithm can make the time complexity to much more faster than O(n)

## Recursion
Recursive function is a function that calls itself.
Stack Overflow: Programming language deals with the nested function with the stack LIFO. 
which means we might encounter some cases that the call the function in the function itself we might use up the memory space 

## Recursion
# Identigy the base case
# Identify the recursive case
# Get closer and closer and return when needed. Ususally you have 2 returns

"""



def inception(counter):
    if counter > 3:
        return 'done'
    counter += 1
    return inception(counter)

counter = 0
print(inception(counter))