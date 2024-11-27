class Graph:
    def __init__(self, graph, heuristic, start_node):
        self.graph = graph            # AND-OR Graph (dictionary form)
        self.heuristic = heuristic    # Heuristic values for nodes
        self.start_node = start_node  # Start node
        self.solved = []              # List of solved nodes
        self.solution = {}            # Optimal solution tree

    def min_cost_child(self, node):
        """ Find the minimum cost child set for an OR node. """
        min_cost = float('inf')
        best_child_set = None

        for child_set in self.graph[node]:
            cost = sum(self.heuristic[child] for child in child_set)
            if cost < min_cost:
                min_cost = cost
                best_child_set = child_set

        return best_child_set

    def ao_star(self, node):
        """ Main AO* Algorithm """
        print(f"Processing Node: {node}")

        if node in self.solved:
            return True

        if node not in self.graph or not self.graph[node]:
            self.solved.append(node)
            return True

        best_child_set = self.min_cost_child(node)
        is_solved = True

        for child in best_child_set:
            if not self.ao_star(child):
                is_solved = False

        if is_solved:
            self.solved.append(node)
            self.solution[node] = best_child_set
            print(f"Node {node} is solved with children: {best_child_set}")

        return is_solved

    def display_solution(self):
        """ Display the optimal solution tree """
        print("\nOptimal Solution Tree:")
        for key in self.solution:
            print(f"{key} --> {self.solution[key]}")

def main():
    graph = {
        'A': [('B', 'C'), ('D',)],   # OR node: A can choose between (B, C) and (D)
        'B': [('E',), ('F',)],       # OR node: B can choose between (E) and (F)
        'C': [],                     # Leaf node
        'D': [('G', 'H')],           # AND node: D must solve both G and H
        'E': [],                     # Leaf node
        'F': [],                     # Leaf node
        'G': [],                     # Leaf node
        'H': []                      # Leaf node
    }

    heuristic = {
        'A': 6, 'B': 2, 'C': 2, 'D': 3,
        'E': 1, 'F': 1, 'G': 1, 'H': 1
    }

    start_node = 'A'

    graph_obj = Graph(graph, heuristic, start_node)

    graph_obj.ao_star(start_node)

    graph_obj.display_solution()

if __name__ == "__main__":
    main()
