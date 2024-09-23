# Practice 1 
# G R A P H S

import os
from collections import defaultdict

class Graph:
    def __init__(self, n_nodes, nodes_names, edges):
        self.graph = defaultdict(list)
        self.n_nodes = n_nodes
        self.nodes_names = nodes_names
        self.edges = edges
        self.create_edges()

    def create_edges(self):
        for edge in self.edges:
            self.add_edge(edge[0], edge[1])
        
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_all_paths(self, start, end, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()

        path.append(start)
        visited.add(start)

        # If we reach the end node, return the current path
        if start == end:
            yield list(path)
        else:
            # Continue to explore neighbors
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    yield from self.find_all_paths(neighbor, end, path, visited)
        
        # Backtrack
        path.pop()
        visited.remove(start)

    def all_paths(self, start, end):
        return list(self.find_all_paths(start, end))

    def shortest_path(self, start, end):
        all_paths = self.all_paths(start, end)
        if all_paths:
            return min(all_paths, key=len)  # The shortest path
        return None
    
    def to_string(self): #Prints adjacency list
        for node, neighbors in self.graph.items():
            print(f"{node} -> {', '.join(neighbors)}")
    
def start_end():#Asks for the start and end node
    start = input("Enter the starting node: ").strip()
    end = input("Enter the end node: ").strip()

    if start == end:
        print("Start node and End node are the same, please select diferent nodes.")
        return start_end()
    return start, end

# Treats the file to separate it between the name of the nodes, the number of nodes and the edges
def file_treatment(file):
    lines = []

    for line in file:
        line = line.strip()
        lines.append(line.split(","))

    n_nodes = lines[0]
    nodes_names = lines[1]
    edges = lines[2:]

    return Graph(n_nodes, nodes_names, edges)

# Verifies that the input is a valid option of the menu
def s_option():
    n = input("Selecct an option: \n")
    if not n.isdigit():
        print("The selected option is invalid, please introduce a valid option.")
        return s_option()
    else:
        n = int(n)

    if n >= 0 and n <= 4:
        return n
    else:
        print("The selected option is invalid, please introduce a valid option.")
        return s_option()

if __name__ == "__main__":
    try: #Tries to open the file
        file = open("input.txt", "r")
    except FileNotFoundError:
        print('File does not exist')
    finally:
        option = None

        graph = file_treatment(file.readlines())
        file.close()

        while option != 0:
            os.system("cls")
            print("*** G R A P H S ***\n")
            print("1. All paths to a node")
            print("2. Shortest path to a node")
            print("3. Adjacency list")
            print("4. All graph information")
            print("0. EXIT")
            
            option = s_option()
            if option == 1:
                start, end = start_end()
                paths = graph.all_paths(start, end)

                if not paths:
                    print(f"No path found from {start} to {end}.")
                else:
                    print(f"All paths from {start} to {end}:")
                    for path in paths:
                        print(" -> ".join(path))

                print("\n\t Press any key to continue.")
                os.system("pause")
            elif option == 2:
                start, end = start_end()
                paths = graph.all_paths(start, end)
    
                if not paths:
                    print(f"No path found from {start} to {end}.")
                else:
                    optimal_path = graph.shortest_path(start, end)
                    if optimal_path:
                        print(f"\nOptimal path from {start} to {end}:")
                        print(" -> ".join(optimal_path))
                    else:
                        print("No optimal path found.")

                print("\n\t Press any key to continue.")
                os.system("pause")
            elif option == 3:
                print("Adjacency List:")
                graph.to_string()
                print("\n\t Press any key to continue.")
                os.system("pause")
            elif option == 4:
                print(f" The graph has {graph.n_nodes[0]} nodes.")
                print(f" Their names:")
                for i in graph.nodes_names:
                    print(f"{i}, ", end="")
                print("\n The graph's adjacency list:")
                graph.to_string()
                print("\n\t Press any key to continue.")
                os.system("pause")