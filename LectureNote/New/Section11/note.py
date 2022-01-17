"""
Graph: Graphs are the data structure that can describe the real world problem
Cyclic/Asyclic
Directed/Undirected
Weighted/UnWeighted

How to Describe Graph
It is built upon the fundamental data structure

## Edge List
graph = [[0,2], [2,3], [2,1],[1,3]]

## Adjacent List
graph = [[2],[2,3],[0,1,3],[1,2]]

##Adjacent Matric
graph = [
    [0,0,1,0],
    [0,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]

graph = {
    0: [0,0,1,0],
    1: [0,0,1,1],
    2: [1,1,0,1],
    3: [0,1,1,0]
}

++ PLUS ++
Relationships 

-- MINUS --
Scaling is hard
"""
s = "ss aa bb"
a,b = s.split(" ",maxsplit=1)
print("hello")