"""
Arrays

Arrays: organize the data sequentially,stored in contiguous memory they have footprint
Lookup: O(1)
Push: O(1)
Insert: O(n)
Delete: O(n)

i.e.
0 Juice
1. Apple
2. Cheese
3. Kale
4. Mango

## Static Arrray vs Dynamic Array
Static Array: we need to specify the memory size of the array before storing the array
Dynamic Array: if we need to add the item we don't need to redefine again instead it dynamically adds the memory allocation
append can be O(n) because there is possibility that it appends the data and reaalocates all the elements to the new memory location.

## Summary
Static, Dynamic Arrays
Big(O)
Static Arrays:
---
Lookup O(1)
Push O(1)
Insert O(n)
Delete O(n)
---

Good at storing data, they are in memory in sequential error
When do you use arrays

PLUS
Fast Lookups
Fast push/pop
Ordered

MINUS
Slow Inserts 
Slow Deletes
Fixed Size(Static): We need to declare the memory ahead of time
"""