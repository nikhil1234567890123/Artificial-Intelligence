import heapq
import math

# Define the grid size
ROW, COL = 9, 10

# Check if a cell is within the grid and unblocked
def is_valid(grid, row, col):
    return 0 <= row < ROW and 0 <= col < COL and grid[row][col] == 1

# Calculate heuristic (Euclidean distance)
def calculate_h_value(row, col, dest):
    return math.sqrt((row - dest[0])**2 + (col - dest[1])**2)

# Trace the path from destination to source
def trace_path(parents, dest):
    path = []
    row, col = dest
    while parents[(row, col)] != (row, col):
        path.append((row, col))
        row, col = parents[(row, col)]
    path.append((row, col))
    path.reverse()
    print("The Path is:", " -> ".join(map(str, path)))

# A* search algorithm
def a_star_search(grid, src, dest):
    if not is_valid(grid, src[0], src[1]) or not is_valid(grid, dest[0], dest[1]):
        print("Invalid source or destination")
        return
    
    if src == dest:
        print("Already at the destination")
        return

    open_list = [(0, src[0], src[1])]
    parents = { (src[0], src[1]): (src[0], src[1]) }
    g_values = { (src[0], src[1]): 0 }

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while open_list:
        _, i, j = heapq.heappop(open_list)

        if (i, j) == dest:
            trace_path(parents, dest)
            return
        
        for d in directions:
            new_i, new_j = i + d[0], j + d[1]
            
            if is_valid(grid, new_i, new_j):
                g_new = g_values[(i, j)] + 1
                f_new = g_new + calculate_h_value(new_i, new_j, dest)
                
                if (new_i, new_j) not in g_values or g_new < g_values[(new_i, new_j)]:
                    g_values[(new_i, new_j)] = g_new
                    heapq.heappush(open_list, (f_new, new_i, new_j))
                    parents[(new_i, new_j)] = (i, j)
    
    print("Failed to find the destination")

def main():
    # Define the grid (1 = unblocked, 0 = blocked)
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    src = (8, 0)
    dest = (0, 0)
    a_star_search(grid, src, dest)

if __name__ == "__main__":
    main()
