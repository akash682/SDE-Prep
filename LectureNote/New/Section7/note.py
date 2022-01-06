"""
Hash Tables
Hash Function is a function which converts the Hash Key into memory location!
This speeds up the process of inserting and retrieving!
Indeponent: hash function is indeponent where you can convert one way from the other but not the other way round.

Hash Map
Search O(1)
Lookup O(1)
Delete O(1)
Search O(1)

## Hash Tables VS Arrays
Arrays
Search O(n)
Lookup O(1)
Push* O(1)
Insert O(n)
Delete O(n)

Hash Tables
Search O(1)
Insert O(1)
Lookup O(1)
Delete O(1)

Problem: No concept of order

Hash Tables
++ PLUS ++
Fast Lookups
Fast Inserts
Flexible Keys

-- MINUS --
Unordered
Slow key Iteration

"""

class User:
    def __init__(self) -> None:
        self.age = 54
        self.name = "Kylie",
        self.magic = True
    
    def scream(self):
        return "ahhh!"

usera = User()
print(usera.name)
print(usera.age)
print(usera.scream())
