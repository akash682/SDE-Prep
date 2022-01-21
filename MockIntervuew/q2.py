TimeComplexity O(n)
SpaceComplexity O(n)

"""
"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
"""

## TestCase
[[0,30],[5,10],[15,20]] 
-> 2 

0-----------------30
  5---10
         15---20

[15, 30]
[[7,10],[2,4]]
  2----4
         7---10
-> 1

[[2,4],[7,10]]
[4]
[10]

[]
--> 0

[[0,5][5,6]]
--> 2

[[0,5][6,7]]
-> 1

Input: integers
Range: starti, endi
  0 <= starti <= 10^4
  0 <= endi <= 10^4
  
## Psudo Code
[0]*len(10^4)
we will add +1 to the index that we have meeting
we can grab the maximum out of this array 

[[0, 4], [2,6], [5,9]]
tmp= [0, 0, 0, 0, 0, 0 ,0 , 0, 0, 0]
[0, 4]
tmp = [1,1,1,1,0,0,0,0,0,0]
[2,6]
tmp = [1,1,2,2,1,1,1,0,0,0]
[]
... 
tmp =
return max(tmp)

## BruteForceApproach
def minmeetingroom(arr):
  # [[7,10],[2,4]]
  fin_max = []
  for i in range(len(arr)):
    fin_max.append(max(arr[i]))
  max_time = max(fin_max) #10
  
  fin_min = []
  for i in range(len(arr)):
    fin_min.append(min(arr[i]))
  min_time = min(fin_min) #2
  
  # [[7,10],[2,4]] --> [[5,8],[0,2]]
  
  for i in range(len(arr)):
    arr[i][0] = arr[i][0] - min_time
    arr[i][1] = arr[i][1] - min_time
  	
  meeting_room_needed = [0]*(max_time-min_time+1) # [0,0,0,0,0,0,0,0,0]O(max-min+1)
  for i in range(len(arr)):
    meeting = arr[i]
    for j in range(meeting[0], meeting[1]+1):
    	meeting_room_needed[j] += 1
  return max(meeting_room_needed)
  
  
https://leetcode.com/problems/meeting-rooms-ii/
  
    
    


## 


```
>>> max([[0, 4], [2,6], [5,9]])
[5, 9]
```
"""

