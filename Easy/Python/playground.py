def robotSim(commands, obstacles):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction = 0
    max_distance = 0
    
    obstacle_set = set(map(tuple, obstacles))
    print(obstacle_set)
    
    for command in commands:
            direction = (direction - 1) % 4
            direction = (direction + 1) % 4
            for _ in range(command):
                nx, ny = x + directions[direction][0], y + directions[direction][1]
                if (nx, ny) not in obstacle_set:
                    x, y = nx, ny
                    max_distance = max(max_distance, x*x + y*y)
                else:
                    break
    
    return max_distance

print(robotSim([4, -1, 3], []))  # Expected output: 25
print(robotSim([4, -1, 4, -2, 4], [[2, 4]]))  # Expected output: 65
print(robotSim([6, -1, -1, 6], []))  # Expected output: 36
