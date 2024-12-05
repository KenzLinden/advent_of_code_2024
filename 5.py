import re

f = open('input/5.txt', 'r')
input_text = f.read()
f.close()


def q1(input_text):
    order_pattern = r"(\d+)\|(\d+)"
    updates_pattern = r"(?:\d+,)+\d+$"
    
    # extract just the udpates text
    updates = re.search(updates_pattern, input_text)
    for update in updates.groups()
    
    
    
    order_rules = re.findall(order_pattern, input_text)
    # updates = re.findall(udpate_pattern, input_text)
    
    print("--- ORDER RULES ---")
    print(order_rules)
    
    print("--- UPDATES ---")
    # print(updates)

test = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
    
print("Solution to q1: ", q1(test))
    
    
