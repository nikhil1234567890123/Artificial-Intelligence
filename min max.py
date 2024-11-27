# Define a class for a Tree Node
class Node:
    def __init__(self, value=None, children=None):
        self.value = value  # value of the node (for leaf nodes)
        self.children = children if children is not None else []  # children nodes

# Minimax function for tree traversal
def minimax(node, depth, is_maximizing):
    # Base case: if leaf node is reached, return its value
    if not node.children:
        return node.value

    # Maximizing player
    if is_maximizing:
        best_value = -float('inf')
        for child in node.children:
            value = minimax(child, depth + 1, False)  # Minimizer's turn next
            best_value = max(best_value, value)
        return best_value

    # Minimizing player
    else:
        best_value = float('inf')
        for child in node.children:
            value = minimax(child, depth + 1, True)  # Maximizer's turn next
            best_value = min(best_value, value)
        return best_value

# Example of using the Minimax algorithm on a tree

# Leaf nodes (terminal nodes with predefined values)
leaf1 = Node(value=3)
leaf2 = Node(value=5)
leaf3 = Node(value=6)
leaf4 = Node(value=9)
leaf5 = Node(value=1)
leaf6 = Node(value=2)
leaf7 = Node(value=9)
leaf8 = Node(value=0)

# Intermediate nodes that connect to the leaf nodes
nodeA = Node(children=[leaf1, leaf2])
nodeB = Node(children=[leaf3, leaf4])
nodeC = Node(children=[leaf5, leaf6])
nodeD = Node(children=[leaf7, leaf8])

# Root node connecting all intermediate nodes
root = Node(children=[nodeA, nodeB, nodeC, nodeD])

# Calling minimax on the root node with initial depth 0 and starting with the maximizer
optimal_value = minimax(root, 0, True)
print("Optimal Value:", optimal_value)
