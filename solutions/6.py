# I won't even lie I was kind of stumped: https://github.com/matheusstutzel/adventOfCode/blob/main/2024/06/p2.py (Original solution)

f = open("input/6.txt", "r")
input_text = f.read()
f.close()

# part
def q1(input_text):
    # locate the guard
    grid = input_text.split()

    movement = {"^": (">", (-1, 0)), ">": ("V", (0, 1)), "V": ("<", (1, 0)), "<": ("^", (0, -1))}
    
    position = (0,0)
    
    # find starting position
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in movement:
                position = (i, j)
                direction= grid[i][j]
                break
    
    # start movement
    while (position[0] >= 0 and position[0] < len(grid)) and (position[1] >= 0 and position[1] < len(grid[position[0]])):
        line = grid[position[0]]
        line = line[:position[1]] + "X" + line[position[1]+1:]
        grid[position[0]] = line
        (new_direction, move) = movement[direction]
        
        new_y = position[0] + move[0]
        new_x = position[1] + move[1]
        
        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[new_y]):
            position = (new_y, new_x)
            continue
        if grid[new_y][new_x] == "#":
            direction = new_direction
            continue
        position = (new_y, new_x)
    
    count = 0
    for i in grid:
        for j in i:
            if j == "X":
                count += 1
                
    return count


# essentially part one but as a function so I can use for part 2 lol
# returns false if route can be escaped
def run_route(grid, position, direction, movement, obstacle):
    visit = set()
    
    while(position[0] >= 0 and position[0] < len(grid) and (position[1] >= 0 and position[1] < len(grid[position[0]]))):
        visit.add((position[0], position[1], direction))
        (new_direction, move) = movement[direction]
        
        new_y = position[0] + move[0]
        new_x = position[1] + move[1]
        
        if (new_y, new_x, direction) in visit:
            return True

        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[new_y]):
            position = (new_y, new_x)
            continue
            
        if grid[new_y][new_x] == "#" or (new_y, new_x) == obstacle:
            direction = new_direction
            continue
        position = (new_y, new_x)
    
    return False

def q2(input_text):
    grid = input_text.split()

    movement = {"^": (">", (-1, 0)), ">": ("V", (0, 1)), "V": ("<", (1, 0)), "<": ("^", (0, -1))}
    
    position = (0,0)
    direction = None
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in movement:
                position = (i, j)
                direction = grid[i][j]
                break
    
    start_position = position
    start_direction = direction
    
    while(position[0] >= 0 and position[0] < len(grid) and (position[1] >= 0 and position[1] < len(grid[position[0]]))):
        line = grid[position[0]]
        line = line[:position[1]] + "X" + line[position[1] + 1:]
        grid[position[0]] = line
        
        (new_direction, move) = movement[direction]
        new_y = position[0] + move[0]
        new_x = position[1] + move[1]
        
        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[new_y]):
            position = (new_y, new_x)
            continue
            
        if grid[new_y][new_x] == "#":
            direction = new_direction
            continue
        position = (new_y, new_x)
    
    obstacle = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                obstacle.append((i, j))
    
    count = 0
    for x in obstacle:
        if run_route(grid, start_position, start_direction, movement, x):
            count += 1
    
    return count
        
    

print("Solution to q1: ", q1(input_text))
print("Solution to q2: ", q2(input_text))
