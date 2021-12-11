# def validity(chunks):
#     track = []
#     completion = []
    # rules = {
    #     "]": ['[',57],
    #     ')': ['(',3],
    #     '}': ['{',1197],
    #     '>': ['<',25137]
    # }
#     penalty = 1
#     opening = ['(', '[', '{', '<']
#     closing = [')', ']', '}', '>']
#     for i in range(len(chunks)):
#         if chunks[i] in opening:
#             track.append(chunks[i])
#         elif chunks[i] in closing:
#             if rules.get(chunks[i])[0] == track[-1]:
#                 track.pop()
#             else:
#                 return rules.get(chunks[i])[1]
    
#     return 0

#################### PART 2 #####################

def validity(chunks):
    track = []
    completion = []
    rules = {
        "]": ['[',57],
        ')': ['(',3],
        '}': ['{',1197],
        '>': ['<',25137]
    }

    completion_rules = {
        "[": [']',2],
        '(': [')',1],
        '{': ['}',3],
        '<': ['>',4]
    }
    penalty = 1
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    for i in range(len(chunks)):
        if chunks[i] in opening:
            track.append(chunks[i])
        elif chunks[i] in closing:
            if rules.get(chunks[i])[0] == track[-1]:
                track.pop()
            else:
                return False
    score = 0
    for i in range(len(track)-1,-1,-1):
        completion.append(completion_rules.get(track[i])[0])
        score *= 5
        score += completion_rules.get(track[i])[1]
    return [score]


f = open("input_files/day10.in")
lines = f.readlines()


# total = 0
scores = []
for line in lines:
    # print(line.strip())
    if validity(line.strip()) != False:
        scores += validity(line.strip())
    # total += validity(line.strip())
# print(total)
scores.sort()
mid = int((len(scores)/2))
print(scores[mid])
