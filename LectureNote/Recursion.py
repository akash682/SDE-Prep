"""
Github folder(Recusive)
Recursion is a function that we call that function itself.

Math for the recursive task is difficult but useful
i.e. Traversing the tree, DOM traversal

Recursion
Scenario: Tap Poaring water & Man in coutch watching TV
Task: Pour the water until the cup gets filled

Stack Overflow: Biggest problem is the infinite loop
Computer needs to allocate memory to rememver the action. If the function is calling itself and returning nothing then we experience infinite loop and which result in Stack overflow.

Recursion
Pros Make a code dry and enhance the readability(Tree traversal)
Cons Large Stack

There are a way to make it memory efficient!

Rucursion Rule
1. Divided into number of subproblems that are smaller instances of the same problem.
2. Each instance of the subproblem is identical in nature
3. The solutions of each subproblem can be combined to solve the problem at hand.
Divide and Conquer using Recursion
"""

counter = 0

def inception(counter):
    if counter > 3:
        return 'done'
    counter += 1
    print('done')
    return inception(counter)

print(inception(counter))

result = 1

def factorial(number):
    global result
    if number == 1:
        return result

    if number != 1:
        tmp = number
        left = factorial(number-1)
    
    result = tmp*left
    return result

print(factorial(5))

# Simple Ans
def factorial_recursive(number):
    if number > 1:
        return number*factorial(number-1)
    
    return number

def factorial_iterative(number):
    res = 1
    for i in range(2, number+1):
        res *= i
    
    return res

print(factorial_recursive(6))
print(factorial_iterative(6))