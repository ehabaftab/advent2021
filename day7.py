f = open("input_files/day7.in")
numbers = f.readlines()
ls = numbers[0].split(",")
crabs = []
for n in ls:
    crabs.append(int(n))

crabs.sort()

#solving this by finding median
print(len(crabs)/2)
print(crabs[499])
print(crabs[500])

min_fuel = 100000000000000000000000000
for i in range (0,2000):
    fuel = 0
    for crab in crabs:
        distance = abs(crab - i)
        fuel += (distance*(distance+1))/2
    if fuel < min_fuel:
        min_fuel = fuel
print(min_fuel)

sum_pos = 0
for crab in crabs:
    sum_pos += crab

print(sum_pos/len(crabs))