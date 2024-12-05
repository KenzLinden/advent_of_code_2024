from collections import defaultdict
import re

f = open('input/5.txt', 'r')
input_text = f.read()
f.close()

# checks if update provided follows specified rules
def valid_update(nums, rules):
    for num in nums:
        if not rules[num]:
            for _, v in rules.items():
                if num in v:
                    v.remove(num)
        else:
            return False      
    return True


# fixes provided list of nums to abide by it's set rules
# THIS SOLUTION IS SO GOOFY AND DUMB BUT I LOVE IT
def fix_update(nums, rules):
    fixed_list = list()
    
    i = 0
    while i < len(nums):
        if not rules[nums[i]]:
            for _, v in rules.items():
                if nums[i] in v:
                    v.remove(nums[i])
            fixed_list.append(nums[i])
            i += 1
        # if misplaced, put at end. Eventually it all sorts itself.
        else:
            misplaced = nums.pop(i)
            
            nums.append(misplaced)
    return fixed_list

# weird solution but quite fun! Other method I thought of was using some form
# of n-tree
def q1(input_text):
    total = 0
    
    order_pattern = r"(\d+)\|(\d+)"
    
    # extract just the udpates text and put in 2d matrix
    update_section = input_text.strip().split('\n\n')[1]
    update_section = update_section.splitlines()
    update_section = [list(map(int, row.split(','))) for row in update_section]

    
    # make a hash map that maps a number to parent values (predecessors)
    # # then map the rules provided (default is empty list)
    order_rules = re.findall(order_pattern, input_text)
    rules = defaultdict(list)
    
    for rule in order_rules:
        rules[int(rule[1])].append(int(rule[0]))
        
    
    # for each number in a line, check that it's parent values have already gone
    for line in update_section:
        temp_rules = defaultdict(list)
        
        # remove parent-child relationships that are missing in line
        for num in line:
            temp_rules[num] = [x for x in rules[num] if x in line]
            
        if(valid_update(line, temp_rules)):
            total += (line[int((len(line)-1)/2)])
    
    return total
        
# part 2
def q2(input_text):
    total = 0
    
    order_pattern = r"(\d+)\|(\d+)"
    
    # extract just the udpates text and put in 2d matrix
    update_section = input_text.strip().split('\n\n')[1]
    update_section = update_section.splitlines()
    update_section = [list(map(int, row.split(','))) for row in update_section]

    
    # make a hash map that maps a number to parent values (predecessors)
    # # then map the rules provided (default is empty list)
    order_rules = re.findall(order_pattern, input_text)
    rules = defaultdict(list)
    
    for rule in order_rules:
        rules[int(rule[1])].append(int(rule[0]))
        
    
    # for each number in a line, check that it's parent values have already gone
    for line in update_section:
        temp_rules = defaultdict(list)
        
        # remove parent-child relationships that are missing in line
        for num in line:
            temp_rules[num] = [x for x in rules[num] if x in line]
            
        # if update format is not valid, fix it
        if not valid_update(line, temp_rules):
            fixed_list = fix_update(line, temp_rules)
            print("FIXED: ", fixed_list)
            total += (fixed_list[int((len(line)-1)/2)])
            
    return total
        
    
print("Solution to q1: ", q1(input_text))
print("Solution to q2: ", q2(input_text))
    
    
