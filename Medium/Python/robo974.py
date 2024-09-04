def robotSim(commands, obstacles):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction = 0
    maxDist = 0
    
    obstacles = set(map(tuple, obstacles))
    
    for command in commands:
        if command == -2:
            direction = (direction - 1) % 4
        elif command == -1:
            direction = (direction + 1) % 4
        else:
            for _ in range(command):
                nx, ny = x + directions[direction][0], y + directions[direction][1]
                if (nx, ny) not in obstacles:
                    x, y = nx, ny
                    maxDist = max(maxDist, x*x + y*y)
                else:
                    break
    
    return maxDist

# Test cases
print(robotSim([4, -1, 3], []))  # Expected output: 25
print(robotSim([4, -1, 4, -2, 4], [[2, 4]]))  # Expected output: 65
print(robotSim([6, -1, -1, 6], []))  # Expected output: 36
