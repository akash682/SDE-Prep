"""
Linear Search
Linear Search is the search in which we perform the search element by element from the beginning of the array.
Time Complexity: O(n)


Binery Search
If the list is the sorted list then we can perform a Binery Search which is backed by divided and conquor.
O(logn)

Traversal 
Traversal is an operation that you are touching every node.
Time Complexity: O(n)

Tree Traversal
Graph Traversal

Breadth First Search: 
Breadth First Search is an search method where you traverse level by level.
i.e. 9 , 4, 20 ,1, 6 ,15 ,170 

Depth First Search
Depth First Search is an search method where the search traverse the branch as deep as possible.
Less memory consumption because we don't need to store the parent node.
i.e. 9, 4, 1, 6, 20, 15, 170

   9
  4 20
1 6 15 170

BFS vs DFS
Time Complexity is the same O(n), but the order matters

BFS:Pros Shortest Path, Closer Nodes || Cons More Memory
DFS:Pros Less Memory, Does Path Exist? || Can get Slow

Exercise
# If you know a solution is not far from the root of the tree: BFS
# If the tree is very deep and solutions are rare: BFS(DFS will take long)
# If the tree is very wide: DFS(BFS will need too much memory)
# If solutionsa re frequent but located deep in the tree: DFS
# Determining whether a path exists between two nodes: DFS
# Finding the shortest path: BFS

BFS needs to keep track of the child nodes to traverse it later on.
"""