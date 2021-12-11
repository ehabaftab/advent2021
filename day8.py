# def seven_segment(output):
    # unique = {
    # 2: '1',
    # 3: '7',
    # 4: '4',
    # 7: '8'
    # }
#     # if sorted("abcegd") == sorted(output):
#     #     return "0"
#     # elif sorted("dafgc") == sorted(output):
#     #     return "2"
#     # elif sorted("dafbc") == sorted(output):
#     #     return "3"
#     # elif sorted("defbc") == sorted(output):
#     #     return "5"
#     # elif sorted("defbgc") == sorted(output):
#     #     return "6"
#     # elif sorted("abcfde") == sorted(output):
#     #     return "9"
#     # else:
#     return unique.get(len(output))
def get_key(val):
    for key, value in display.items():
         if val == value:
             return key

unique = {
    2: [6,5],
    3: [0,6,5],
    4: [1,2,6,5],
    7: [0,1,2,3,4,5,6]
    }

display = {
    0: ['a'],
    1: ['b'],
    2: ['c'],
    3: ['d'],
    4: ['e'],
    5: ['f'],
    6: ['g']
}


#   0 00 0
#   1    6
#   1    6
#     22
#   3    5
#   3    5
#   4 44 4


f = open("input_files/day8.in")
output = []
for line in f:
    output.append(line.split("|")[1])

print(get_key('d'))


# final = 0
unique_len = [2,3,4,7]
for out in output:
    output = ''
    split = out.strip().split()
    done = False
    while not done:
        for i in range(len(split)):
            if len(split[i]) == 2:
                display[unique.get(2)[0]] = split[i][0]
            
# print(final)