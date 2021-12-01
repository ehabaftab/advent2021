f = open("input_files/day1.in")
count = 0
previous = 0
entries = f.readlines()
i = 0
while len(entries) - i >= 3:
    e1 = int(entries[i])
    e2 = int(entries[i+1])
    e3 = int(entries[i+2])
    if(e1+e2+e3 > previous and i > 0):
        count += 1
    previous = e1+e2+e3
    i += 1


print(count)