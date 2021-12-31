strings = ['a', 'b', 'c', 'd'] # 4*4s= 16 bytes

# Lookup O(1)
# Since the data is stored contiguously the RAM immediately know where to grab the data when the index specified
print(strings[2]) 

# Push O(1)
strings.append('e')
print(strings)

# Pop O(1)
strings.pop()
print(strings)

# Insert  O(n), we need to shift the whole data allocation by 1, which makes it do an operation for each element, which makes the time complexity O(n)
strings.insert(0,'z')
print(strings)


