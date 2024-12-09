f = open("input/6.txt", "r")
input_text = f.read()
f.close()

def rotate_90(direction):
    if direction == "^":
        return ">"
    if direction == ">":
        return "V"
    if direction == "V":
        return "<"
    return "^"

def q1(input_text):
    # locate the guard
    grid = input_text.split()
    
    ocation = [-1, -1]
    for i, line in enumerate(grid):
        for j, item in enumerate(line):
            if item == "^":
                location = [i, j] # y x kind of. line then location.
    
    direction = "^"
    
    while ((0 <= location[0] <= len(grid)-1) and (0 <= location[1] <= len(grid[0]) - 1)):
        if direction == "^":
            if grid[location[0]-1][location[1]] is not "#":
                location
        elif direction == ">":
            print("Right")
        elif direction == "<":
            print("Left")
        else:
            print("Down")
        break
    return

print("Solution to q1: ", q1(input_text))
