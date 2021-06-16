"""
Graph: Good to express real world relationship

Node: Node(Vertex), Edge
i.e. Network, Friendships, Roads

Directed/Undirected
Directed: describes the information of the flow relationship(i.e One way Road, Twitter)
Undirected: no info about direction(i.e. Facebook)

Weighted/Unweighted
Information on the Edges! 
i.e. Go to the destination in more efficient way, to find the shorter path

Cyclic/Acyclic
When Nodes are connected in circular fashion
Google Maps

Edge List: Just shows the connection and the node which is a list of edge 
Adjacent List: shows the adjacent node of the specific node
Adjacent Matrix: 
"""
# Edge List
graph = [[0,2], [2,3],[2,1],[1,3]]

# Adjacent List (Hash Table)
graph = [[2],[2,3],[0,1,3],[1,2]]

#Adjacent Matrix
graph = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
