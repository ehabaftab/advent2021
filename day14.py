def step(string):
    i = 0
    while i < len(string):
        if i+2 < len(string)+1:
            insert = rules.get(string[i:i+2])
            temp = list(string)
            temp.insert(i+1,insert)
            string = ''.join(temp)
            i += 1
        i += 1
    return string

def common(string):
    count = {}
    ls = list(string)
    for i in range(len(ls)):
        try:
            count[ls[i]] += 1
        except:
            count[ls[i]] = 1
    maximum = 0
    minimum = 10000000000
    for key in count:
        if count[key] > maximum:
            maximum = count[key]
        if count[key] < minimum:
            minimum = count[key]
        
    return(maximum,minimum)

f = open("input_files/day14.in")
lines = f.readlines()
rules = {}
starting = 'SCSCSKKVVBKVFKSCCSOV'

for line in lines:
    rule = line.strip().split('->')
    rules[rule[0].strip()] = rule[1].strip()

for i in range(10):
    starting = step(starting)


# print(starting)
answer = common(starting)
print(answer)
print(answer[0]-answer[1])