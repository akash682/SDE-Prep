"""
Blocks = [
    {
        "gym": false,
        "school": true,
        "store":false
    },
    {
        "gym": true,
        "school": false,
        "store":false
    },
    {
        "gym": true,
        "school": true,
        "store":false
    },
    {
        "gym": false,
        "school": true,
        "store":false
    },
        {
        "gym": false,
        "school": true,
        "store":true
    }
]

Reqs = ["gym", "school"]
min(max(dist(Block1-gym), dist(Block1-school)), ... ,]

Block[0] --> max(1,0) = 1
Block[1] --> max(0,1) = 1
Block[2] --> max(0,0) = 0
Block[3] --> max(1,0) = 1
Block[4] --> max(2,0) = 2

min(1,1,0,1,2) = 0
"""

Blocks = [
    {
        "gym": False,
        "school": True,
        "store":False
    },
    {
        "gym": True,
        "school": False,
        "store":False
    },
    {
        "gym": True,
        "school": True,
        "store":False
    },
    {
        "gym": False,
        "school": True,
        "store":False
    },
        {
        "gym": False,
        "school": True,
        "store":True
    }
]

Reqs = ["gym"]
#Brute Force Approch

gym_arr =[0,1,1,0,0]
res_arr = []
distance = 0
for i in range(len(gym_arr)):
    while i-distance >=0 or i+distance <=len(gym_arr)-1:
        if i-distance >=0 and gym_arr[i-distance] == 1:
            res_arr.append(distance)
            break
        if i+distance <= len(gym_arr)-1 and gym_arr[i+distance] == 1:
            res_arr.append(distance)
            break 
        distance +=1

print(res_arr)
        

