def find(j,i,pi,pj):
    pi = i
    pj = j
    done = False
    while not done:
            found = False
            for k in range(1,-2,-2):
                try:
                    if board[j][i] >= board[j][i+k] and i+k != -1:
                        found = True
                except:
                    continue
            
            for k in range(1,-2,-2):
                try:
                    if board[j][i] >= board[j+k][i] and j+k != -1:
                        found = True
                except:
                    continue
            
            if found == False:
                return (j,i)


            for k in range(1,-2,-2):
                try:
                    if board[j][i] >= board[j][i+k] and i+k != -1 and i+k != pi :
                        i += k
                except:
                    continue
            
            for k in range(1,-2,-2):
                try:
                    if board[j][i] >= board[j+k][i] and j+k != -1 and j+k != pj :
                        j += k
                except:
                    continue
            return find(j,i,pi,pj)


def find_basin(j,i,ls):
    lis = []
    done = False
    pi = i
    pj = j

    while not done:
            found = False
            if board[j][i] != 9  and (j,i) not in ls:
                ls.append((j,i))
                found = True
            if found == False:
                return ls


            for k in range(1,-2,-2):
                # print(j,i,k)
                try:
                    if board[j][i+k] != 9 and i+k != -1 :
                        ls = find_basin(j,i+k,ls)
                except:
                    continue    
            
            for k in range(1,-2,-2):
                try:
                    if board[j+k][i] != 9 and j+k != -1 :
                        ls = find_basin(j+k,i,ls)
                except:
                    continue
            # return ls
        
# j+k/i+k != pi/pj makes sure we dont go back where we came from if the numbers are the same

f = open("input_files/day9.in")
lines = f.readlines()
board = [[int(lines[j][i]) for i in range(len(lines[0].strip()))] for j in range(len(lines))]

low_points = []

for row in board:
    print(row)


for j in range(len(lines)):
    for i in range(len(lines[0].strip())):
        if find(j,i,0,0) not in low_points:
            low_points.append(find(j,i,0,0))

sum_low = 0
for points in low_points:
    sum_low += board[points[0]][points[1]] + 1

print(sum_low)

largest = []
size = 1
count = 0
for low in low_points:
    largest.append(len(find_basin(low[0],low[1],[])))
    count += 1

largest.sort()

for i in range(-1,-4,-1):
    size *= largest[i]


print(largest)
print(count)
print(size)

