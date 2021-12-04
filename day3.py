# f = open("input_files/day3.in")
# commands = f.readlines()
# gamma = ''
# epsilon = ''
# ones = 0
# zeros = 0
# for i in range(len(commands[0].strip())):
#     for line in commands:
#         if int(line[i]) == 1:
#             ones += 1
#         elif int(line[i]) == 0:
#             zeros += 1 

#     if ones > zeros:
#         gamma += '1'
#         epsilon += '0'
#     else:
#         gamma += '0'
#         epsilon +='1'
#     ones = 0
#     zeros = 0 
# print(int(gamma,2)*int(epsilon,2)) 


#################################################################

f = open("input_files/day3.in")
commands = f.readlines()
gamma = ''
epsilon = ''
ones = 0
zeros = 0
o2 = commands.copy()
co2 = commands.copy()
for i in range(len(commands[0].strip())):
    for line in o2:
        if int(line[i]) == 1:
            ones += 1
        elif int(line[i]) == 0:
            zeros += 1 
    if ones > zeros or ones == zeros:
        j = 0
        while j < len(o2):
            if int(o2[j].strip()[i]) == 0:
                o2.pop(j)
                j = -1
            j += 1


    else:
        j = 0
        while j < len(o2):
            if int(o2[j].strip()[i]) == 1:
                o2.pop(j)
                j = -1
            j += 1

    ones = 0
    zeros = 0 
    for line in co2:
        if int(line[i]) == 1:
            ones += 1
        elif int(line[i]) == 0:
            zeros += 1 

    if ones > zeros or ones == zeros:
        j = 0
        while j < len(co2) and len(co2) != 1:
            if int(co2[j].strip()[i]) == 1:
                co2.pop(j)
                j = -1
            j += 1


    else:
        j = 0
        while j < len(co2) and len(co2) != 1:
            if int(co2[j].strip()[i]) == 0:
                co2.pop(j)
                j = -1
            j += 1
    ones = 0
    zeros = 0 

print(int(o2[0].strip(),2)*int(co2[0].strip(),2))

print(o2)
print(co2)