f = open("day1.in")
previous = -2
count = 0
entries = f.readlines()
i = 0
while len(entries) - i >= 3:
    e1 = int(entries[i])
    e2 = int(entries[i+1])
    e3 = int(entries[i+2])
    if(e1+e2+e3 > previous):
        count += 1
    previous = e1+e2+e3
    i += 1


print(count)