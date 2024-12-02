f = open("input/2.txt")
input_text = f.read()

# returns true if report input is safe
def report_is_safe(report):
    differences = []
    
    for i in range(len(report)-1):
        differences.append(report[i+1] - report[i])
    
    # just check that all differences calulated followed the distances rules
    if all(-3 <= val <= -1 for val in differences) or all(1 <= val <= 3 for val in differences):
        return True
    return False
    

# part one
def q1(input_text):
    lines = input_text.split('\n')

    total_safe = 0
    for line in lines:
        report = [int(num) for num in line.split()]
        
        if(report_is_safe(report)):
            total_safe += 1
        
    return total_safe

# part two
def q2(input_text):
    lines = input_text.split('\n')
    total_safe = 0
    
    for line in lines:
        report = [int(num) for num in line.split()]
        
        # check if report itself is safe or version of list with one missing element is safe
        if(report_is_safe(report) or any(report_is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))):
            total_safe += 1
    
    return(total_safe)
    

print("Solution to q1: ", q1(input_text))
print("Solution to q2: ", q2(input_text))

f.close()