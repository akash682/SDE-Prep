import math
from traceback import print_tb
print(math.log(243,3))

import heapq
s = [6,7,8,34,5]
print(s.pop())
print(heapq.heappop(s))
heapq.heapify(s)
print(heapq.heappop(s))

dict_a = {
    "a" : 2,
    "b" : 1
}

print(dict_a.keys())