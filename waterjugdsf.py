def DFS(a, b, target):
    # Stack for DFS
    stack = [(0, 0)]
    visited = set()
    path = []

    while stack:
        x, y = stack.pop()
        
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path.append((x, y))

        if x == target or y == target:
            # Add the final state
            if x == target and y != 0:
                path.append((x, 0))
            elif y == target and x != 0:
                path.append((0, y))
            
            for state in path:
                print(f"({state[0]}, {state[1]})")
            return

        # Generate possible states
        stack.extend([
            (a, y),  # Fill Jug1
            (x, b),  # Fill Jug2
            (x - min(x, b - y), y + min(x, b - y)),  # Pour Jug1 -> Jug2
            (x + min(y, a - x), y - min(y, a - x)),  # Pour Jug2 -> Jug1
            (0, y),  # Empty Jug1
            (x, 0)   # Empty Jug2
        ])

    print("No solution")

# Driver code
if __name__ == '__main__':
    Jug1, Jug2, target = 4, 3, 2
    print("Path from initial state to solution state ::")
    DFS(Jug2, Jug1, target)
