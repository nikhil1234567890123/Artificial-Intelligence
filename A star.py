import heapq

class Node:
    def __init__(self, name, g, h):
        self.name = name
        self.g = g  # Cost from start to the current node
        self.h = h  # Heuristic cost from current node to goal
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f  # Compare nodes based on total cost

def a_star_search(start, goal, graph, heuristics):
    open_list = []
    start_node = Node(start, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    g_costs = {start: 0}  # Costs from start node
    parent_map = {start: None}  # Track the path
    
    closed_list = set()  # Visited nodes

    while open_list:
        current_node = heapq.heappop(open_list)
        current_name = current_node.name

        if current_name == goal:
            # Path reconstruction
            path = []
            while current_name:
                path.append(current_name)
                current_name = parent_map[current_name]
            return path[::-1]  # Reverse the path

        closed_list.add(current_name)

        for neighbor, cost in graph[current_name]:
            if neighbor in closed_list:
                continue  # Skip already evaluated neighbors

            tentative_g_cost = g_costs[current_name] + cost

            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                neighbor_node = Node(neighbor, tentative_g_cost, heuristics[neighbor])
                heapq.heappush(open_list, neighbor_node)
                parent_map[neighbor] = current_name

    return None  # No path found

def main():
    graph = {}
    num_edges = int(input("Enter the number of edges in the graph: "))
    
    for _ in range(num_edges):
        edge = input("Enter edge and cost (format: node1 node2 cost): ").split()
        node1, node2, cost = edge[0], edge[1], float(edge[2])
        graph.setdefault(node1, []).append((node2, cost))
        graph.setdefault(node2, []).append((node1, cost))

    heuristics = {}
    for node in graph:
        heuristic_value = float(input(f"Enter heuristic value for node {node}: "))
        heuristics[node] = heuristic_value

    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")

    path = a_star_search(start_node, goal_node, graph, heuristics)
    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")

if __name__ =="__main__":
    main()
