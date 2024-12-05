from collections import defaultdict

# I HATE THIS SOLUTION... IT IS SO UGLY AND I DID NOT MAKE IT NEAT AND NICE...


f = open("input/4.txt")
input_text = f.read()
f.close()

def horizontal_check(input_arrays, y, x):
    i = y
    j = x

    output = [False, False]
    
    try:
        pos_text = input_arrays[i][j] + input_arrays[i][j+1] + input_arrays[i][j+2] + input_arrays[i][j+3] 
        if pos_text == 'XMAS':
            output[0] = True
    except IndexError:
        output[0] = False
    
    try:
        if j >= 3:
            neg_text = input_arrays[i][j] + input_arrays[i][j-1] + input_arrays[i][j-2] + input_arrays[i][j-3] 
            if neg_text == 'XMAS':
                output[1] = True
    except IndexError:
        output[1] = False
    
    return output


def vertical_check(input_arrays, y, x):
    i = y
    j = x
    
    output = [False, False]
    
    try:
        pos_text = input_arrays[i][j] + input_arrays[i+1][j] + input_arrays[i+2][j] + input_arrays[i+3][j] 
        if pos_text == 'XMAS':
            output[0] = True
    except IndexError:
        output[0] = False
    
    try:
        if i >= 3:
            neg_text = input_arrays[i][j] + input_arrays[i-1][j] + input_arrays[i-2][j] + input_arrays[i-3][j]
            if neg_text == 'XMAS':
                output[1] = True
    except IndexError:
        output[0] = False
        
    return output


def diagnol_check(input_arrays, y, x):
    i = y
    j = x
    output = [False, False, False, False]
    
    try:
        if i >= 3:
            text = input_arrays[i][j] + input_arrays[i-1][j+1] + input_arrays[i-2][j+2] + input_arrays[i-3][j+3]
            if text == 'XMAS':
                output[0] = True
    except IndexError:
        output[0] = False
    
    try:
        text = input_arrays[i][j] + input_arrays[i+1][j+1] + input_arrays[i+2][j+2] + input_arrays[i+3][j+3]
        if text == 'XMAS':
            output[1] = True
    except IndexError:
        output[1] = False
        
    try:
        if j >= 3:
            text = input_arrays[i][j] + input_arrays[i+1][j-1] + input_arrays[i+2][j-2] + input_arrays[i+3][j-3]
            if text == 'XMAS':
                output[2] = True
    except IndexError:
        output[2] = False
    
    try:
        if i >= 3 and j >= 3:
            text = input_arrays[i][j] + input_arrays[i-1][j-1] + input_arrays[i-2][j-2] + input_arrays[i-3][j-3]
            if text == 'XMAS':
                output[3] = True
    except IndexError:
        output[3] = False
    
    return output

    
# part 1
def q1(input_text):
    lines = input_text.splitlines()
    total = 0
    
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            hor = horizontal_check(lines, y, x)
            ver = vertical_check(lines, y, x)
            diag = diagnol_check(lines, y, x)

            for val in hor:
                if val:
                    # print("hor", y, x, hor)
                    total += 1
            
            for val in ver:
                if val:
                    # print("ver", y, x, ver)
                    total += 1
            
            for val in diag:
                if val:
                    # print("diag", y, x, diag)
                    total += 1
    
    return total


def q2(input_text):

    lines = input_text.splitlines()

    total = 0


    for y in range(1, len(lines) - 1):  # Avoid out-of-bounds by limiting range
        for x in range(1, len(lines[y]) - 1):  # Same for x
            
            if lines[y][x] == 'A':
                
                found_letters = defaultdict(int)
                
                # Check the diagonals around the center 'A'
                for i, j, k, l in [(-1, -1, 1, 1), (-1, 1, 1, -1)]:
                    
                    # diag must form word "mas"
                    if lines[y+i][x+j] == lines[y+k][x+l]:
                        break
                    
                    letter = lines[y + i][x + j]
                    found_letters[letter] += 1
  
                    letter = lines[y + k][x + l]
                    found_letters[letter] += 1
                    
                # Validate the pattern: 2 'M's and 2 'S's
                if found_letters['M'] == 2 and found_letters['S'] == 2:

                    total += 1


    return total
                        
                        
    


# print("Solution to q1: ", q1(input_text))
print("Solution to q2: ", q2(input_text))

