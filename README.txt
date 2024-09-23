    COMPUTATIONAL THEORY AND COMPLEXITY

PRACTICE 1: GRAPHS
500 CIB
Flores Arenas Marcos Fabian
Ordoñez Contreras Elias
Sosa Hernandez Saul Waldemar
Soto Natera Sebastian

The python file reads the "input.txt" file located on the same directory.
The file needs to contain:
    1st line: Number of nodes or vertices in the graph
    2nd line: Name or identifier for each node
    3th to n line: Edges or transitions between nodes (each transition on a different line)

**You can try different files by either replacing the content of the "input.txt" file or
by changing the name of the "open" function located in line 102 and running the code again.
We recommend to use the second option due to avoid losing any data and comparing easily.**

There are some extra examples on the same folder as requested by the professor.
"input1.txt" corresponds to the desing that CANNOT be cycled, "input2.txt" corresponds to
the desing that CAN be cycled. Each one has its own visual representation.

The program models a graph by initializing an adjacency list with the information on the
file mentioned before.
It utilices a class object named "Graph" for it to contain all necessary functions to the 
construction and reading of the graph.

As the program starts running you will be presented a menu displaying 5 options:
    1. All paths to a node
    2. Shortest path to a node
    3. Adjacency list
    4. All graph information
    0. EXIT
The user will need to choose a valid option in order to continue.

For option 1 and 2, the user will be asked to type the name or identifier of the starting
node and final node (destination node).
In option 1 it will display all existing paths to that node.
In option 2 it will display only the optimal path (if it exists)

For option 3, the entire adjacency list will be displayed.

For option 4, it will display the number of nodes, each one of their names/identifiers, 
and the adjacency list.


--All functions have comments for better understanding--

