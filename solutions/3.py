import re

f = open("input/3.txt")
input_text = f.read()
f.close()

# part 1
def q1(input_text):
    pattern = r'mul\((\d+),(\d+)\)'
    
    total = 0
    for nums in re.findall(pattern, input_text):
        total += (int(nums[0]) * int(nums[1]))
    
    return total

test_input = "do()xmul(2,4)&mul[3,7]!^mul(2,1)don't()don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# part 2
def q2(input_text):
    
    input_text = "do()" + input_text + "don't()" # just nicer to wrap
    input_text = input_text.strip()
    activated_pattern = r"do\(\)(.*?)don't\(\)" # only gets items between do()...don't()
    matches = re.findall(activated_pattern, input_text)
    


    
    total = 0
    nums_pattern = r'mul\((\d+),(\d+)\)'
    for match in matches:
        for nums in re.findall(nums_pattern, match):
            total += (int(nums[0]) * int(nums[1]))


    return total 

print("Solution to q1: ", q1(input_text))
print("Solution to q2: ", q2(input_text))



