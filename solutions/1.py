from collections import defaultdict

f = open('input/1.txt', 'r')
input_text = f.read()

# part 1 - distance score
def q1(input_text):
    lines = input_text.splitlines()
    
    # neat in one line
    list_one, list_two = map(list, zip(*(map(int, line.split('   ')) for line in lines)))

    # inefficient lol
    list_one.sort()
    list_two.sort()
    
    # they should be same length
    total_diff = (sum(abs(a - b) for a,b in zip(list_one, list_two)))
                
    return(total_diff)



# part two - similarity score
def q2(input_text):
    lines = input_text.splitlines()
    list_one, list_two = map(list, zip(*(map(int, line.split('   ')) for line in lines)))

    # we can use hash-map to make it O(n+m) instead of O(n*m) nested for loop
    ids = defaultdict(int)
    
    for id in list_two:
        ids[id] += 1
    
    sim_score = sum((id*ids[id]) for id in list_one)

    return sim_score
        


print("Solution to q1: ", q1(input_text))
print("Solution to q2: ", q2(input_text))
f.close()