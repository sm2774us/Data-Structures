# ALGORITHMS

_____________

## Graph Algorithms

### What is a Graph ?

A **graph** consists of a finite set of **vertices** or nodes and a set of **edges** connecting these vertices. Two vertices are said to be **adjacent** if they are connected to each other by the same edge.

Some basic definitions related to graphs are given below. You can refer to Figure 1 for examples.

- Order: The number of vertices in the graph
- Size: The number of edges in the graph
- Vertex degree: The number of edges that are incident to a vertex
- Isolated vertex: A vertex that is not connected to any other vertices in the graph
- Self-loop: An edge from a vertex to itself
- Directed graph: A graph where all the edges have a direction indicating what is the start vertex and what is the end vertex
- Undirected graph: A graph with edges that have no direction
- Weighted graph: Edges of the graph has weights
- Unweighted graph: Edges of the graph has no weights

![Fig 1. Visualization of Terminology of Graphs](images/algorithms_fig_1_visualization_of_terminology_of_graphs.png)
###### Fig 1. Visualization of Terminology of Graphs

### 1. Breadth-first search

___Traversing___ or ___searching___ is one of the fundamental operations which can be performed on graphs. In **breadth-first search (BFS)**, we start at a particular vertex and explore all of its neighbours at the present depth before moving on to the vertices in the next level. Unlike trees, graphs can contain cycles (a path where the first and last vertices are the same). Hence, we have to keep track of the visited vertices. When implementing BFS, we use a queue data structure.

Figure 2 denotes the animation of a BFS traversal of an example graph. Note how vertices are discovered (yellow) and get visited (red).

![Fig 2. Animation of BFS traversal of a graph](images/algorithms_fig_2_animation_of_BFS_traversal_of_a_graph.gif)
###### Fig 2. Animation of BFS traversal of a graph

#### Applications

### 2. Depth-first search

_____________
 