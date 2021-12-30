"""
BIGO
BIG O asympothic analysis: how well a problem is solved

Good Code
1. Readable
2. Scalable (Big O)

coder is a someone that we give a intructions through a code
Simlar to kitchen, we need to give the intructions to get the output 

To make sure the code is efficient regardless of the computer or to check the scalability of the code 
Big O is a measure to check when the input scales bigger and bigger how slower it the program gets.
How does our runtime grows when the our input gets larger.

Rule1 Worst Case: we cannot be certain of what the input will be so we will only care about the worst case
Rule2 Remove Constants: We drop the constants and the lower dominants because it is insignificant when the input grows.
Rele3 Different terms for inputs: Just because it is using the same time complexity, we don't just add up with same variable.
Rele4 Drop Non Dominants: We only care about the most significant term. We just worry about the scalability.

IF there is a nested loop the big o notation will be quadratic.
As the number of elements increases, the time complexity increases significantly than O(n).

for i in range():
    for j in range():
        xxxx
--> O(n^2)
"""


"""
#Big O Cheat Sheet:
-Big Os-
O(1) Constant- no loops
O(log N) Logarithmic- usually searching algorithms have log n if they are sorted (Binary Search)
O(n) Linear- for loops, while loops through n items
O(n log(n)) Log Liniear- usually sorting operations
O(n^2) Quadratic- every element in a collection needs to be compared to ever other element. Two
nested loops
O(2^n) Exponential- recursive algorithms that solves a problem of size N
O(n!) Factorial- you are adding a loop for every element

Iterating through half a collection is still O(n)
Two separate collections: O(a * b)

-What can cause time in a function?-
Operations (+, -, *, /)
Comparisons (<, >, ==)
Looping (for, while)
Outside Function call (function())

-Rule Book-
Rule 1: Always worst Case
Rule 2: Remove Constants
Rule 3: Different inputs should have different variables. O(a+b). A and B arrays nested would be
O(a*b)
+ for steps in order
* for nested steps
Rule 4: Drop Non-dominant terms

-What causes Space complexity?-
Variables
Data Structures
Function Call
Allocation

O(n!) 

To make the code scalable we want to make time complexity, space complexity efficient.
Readable, Speed(Time Complexity), Memory(Space Complexity)
There is a tradeoff between speed and memory, if we need a speed we need to get rid of some efficiency in the memory

def boo(n):
    for i in range(len(n)):
        print("boo")

boo([1,2,3,4,5]) //O(1)

def arrayofHinTimes(n):
    hiarray = []
    for i in range(len(n)):
        hiarray.append(i)

arrayofHinTimes(6) //O(n)

array = ["hi", "my", "teddy"]
array[0] //O(1)
array[len(array)-1] //O(1)

len(array) //O(n) but in JS array has the information of length in the object, which makes it O(1)

Section Summary
Big O which function is best in terms of readablity and scalablity
why do you care? Time and Memory is a critical problem which makes significant in the cost, they can save a lot of money
Each one is the trade off between speed and memory(time complexity and space complexity)

"""