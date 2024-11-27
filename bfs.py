import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic

    # Comparison based on heuristic value for priority queue
    def __lt__(self, other):
        return self.heuristic < other.heuristic

def best_first_search(start, goal, graph, heuristics):
    # Initialize the priority queue with the start node
    queue = []
    heapq.heappush(queue, Node(start, heuristics[start]))
    
    visited = set()  # Set to track visited nodes
    parent_map = {start: None}  # Map to reconstruct the path

    while queue:
        # Get the node with the lowest heuristic
        current_node = heapq.heappop(queue)

        # If the goal is found, reconstruct the path
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = parent_map[current_node.name]
            return path[::-1]  # Return path in the correct order

        visited.add(current_node.name)

        # Expand the neighbors of the current node
        for neighbor in graph[current_node.name]:
            if neighbor not in visited:
                heapq.heappush(queue, Node(neighbor, heuristics[neighbor]))
                parent_map[neighbor] = current_node

    return None  # Return None if no path is found

def main():
    # Construct the graph
    graph = {}
    num_edges = int(input("Enter the number of edges in the graph: "))
    for _ in range(num_edges):
        node1, node2 = input("Enter edge (format: node1 node2): ").split()
        graph.setdefault(node1, []).append(node2)  # Add node2 to node1's adjacency list
        graph.setdefault(node2, []).append(node1)  # Add node1 to node2's adjacency list

    # Get heuristic values for each node
    heuristics = {}
    for node in graph:
        heuristics[node] = float(input(f"Enter heuristic value for node {node}: "))

    # Input start and goal nodes
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")

    # Perform best-first search and output the result
    path = best_first_search(start_node, goal_node, graph, heuristics)
    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")

if __name__ == "__main__":
    main()
