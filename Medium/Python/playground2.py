#!/usr/bin/env python3

def robot(commands, obstacles):
    direction = 0

    position = [0, 0]
    maxPosition = [0, 0]

    directionDict = {

        0 : "f",
        1 : "r",
        -3 : "r",
        -2 : "d",
        2 : "d",
        3 : "l",
        -1 : "l"
    }

    def dealObstacle(currentPos, going, obs, units):
        leftOrRight = 1

        if going == "d" or going == "l":
            leftOrRight = -1

        if going == "d" or going == "f":
            index = 1
        
        else:
            index = 0
        
        for i in range(units):

            # print(currentPos, end=" ")
            # print("Obstacles: => ", obs)

            if currentPos in obs and i != 0:
                currentPos[index] = currentPos[index] - (1 * leftOrRight)
                print(currentPos)
                break

            currentPos[index] = currentPos[index] + (1 * leftOrRight)
        
        return currentPos


    for num in commands:

        if num < 0:

            if direction == 0 and num == -2:
                direction = direction + 3
            
            else:
                if num == -1:
                    direction = direction + 1
                elif num == -2:
                    direction = direction - 1

        else:
            where = directionDict[direction % 4]
            # print(where, direction)

            position = dealObstacle(position, where, obstacles, num)
            # print(position, maxPosition)
            # print((position[0]**2) + (position[1]**2), (maxPosition[0]**2) + (maxPosition[1]**2))
    
            if (position[0]**2) + (position[1]**2) > (maxPosition[0]**2) + (maxPosition[1]**2):
                maxPosition = [num for num in position]
                # maxPosition = position

            # print("Max => ", maxPosition, end="\n\n")


    # print("FINAL MAX => ", maxPosition, end="\n\n")
    return (maxPosition[0]**2 + maxPosition[1]**2)

# print(robot([4,-1,3], []))
# print(robot([-2, 3, -2, 2], []))
# print(robot([4, -1, 4], [[2, 4]]))
# print(robot([4, -1, 4, -1, 4], [[2, 4]]))
print(robot([4,-1,4,-2,4], [[2,4]]))

