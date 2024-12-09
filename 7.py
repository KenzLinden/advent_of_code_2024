# THIS ONE IS SO SLICK

import re

f = open("input/7.txt", "r")
input_text = f.read()
f.close()

def mult(x, y):
    return(x*y)

def add(x, y):
    return(x+y)

def concatenate(x, y):
    return(int(str(x) + str(y)))

def apply_operations(nums, operations, totals):
    if len(nums) == 1:
        return nums[0]
        
    for operation in operations:
        new_nums = [operation(nums[0], nums[1])] + nums[2:]
        totals.append(apply_operations(new_nums, operations, totals))
    
# part 1
def q1(input_text):
    lines = [line.strip() for line in input_text.strip().split("\n")]
    
    operations = [mult, add]
    
    total_count = 0
    for line in lines:
        nums = re.findall("(\d+)", line)
        nums = [int(x) for x in nums]
        target = nums[0]

        
        totals = list()
        apply_operations(nums[1:], operations, totals)
        
        
        for x in totals:
            if x == target:
                total_count += x
                break
    
    return total_count

# part 2
def q2(input_text):
    lines = [line.strip() for line in input_text.strip().split("\n")]
    
    operations = [mult, add, concatenate]
    
    total_count = 0
    for line in lines:
        nums = re.findall("(\d+)", line)
        nums = [int(x) for x in nums]
        target = nums[0]
        
        totals = list()
        apply_operations(nums[1:], operations, totals)
        
        for x in totals:
            if x == target:
                total_count += x
                break
    
    return total_count

print("Solution to q1: ", q1(input_text))
print("Solution to q2: ", q2(input_text))