# f = open("input_files/day2.in")
# commands = f.readlines()
# depth = 0
# horizontal = 0
# for line in commands:
#     cmd = line.strip().split()
#     if cmd[0] == "up":
#         depth -= int(cmd[1])
#     if cmd[0] == "forward":
#         horizontal += int(cmd[1])
#     if cmd[0] == "down":
#         depth += int(cmd[1])

# print(depth*horizontal)

#############################################

f = open("input_files/day2.in")
commands = f.readlines()
depth = 0
horizontal = 0
aim = 0
for line in commands:
    cmd = line.strip().split()
    if cmd[0] == "up":
        aim -= int(cmd[1])
    if cmd[0] == "forward":
        horizontal += int(cmd[1]) 
        depth += int(cmd[1]) * aim
    if cmd[0] == "down":
        aim += int(cmd[1])

print(depth*horizontal)
