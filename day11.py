
def flash(flash_list,flashes):
    done = False
    flashes = len(flash_list)
    while not done:
            for i,j in flash_list:
                
                found = False
                for k in range(1,-2,-2):
                    new_ls = []
                    try:
                        if board[i][j+k] != 0 and j+k != -1:
                            board[i][j+k] += 1
                            if board[i][j+k] == 10 :
                                board[i][j+k] = 0
                                new_ls.append((i,j+k))
                                flashes += flash(new_ls,flashes)
                    except:
                        continue    
                
                for k in range(1,-2,-2):
                    new_ls = []
                    try:
                        if board[i+k][j] != 0 and i+k != -1:
                            board[i+k][j] += 1
                            if board[i+k][j] == 10 :
                                board[i+k][j] = 0
                                new_ls.append((i+k,j))
                                flashes += flash(new_ls,flashes)
                    except:
                        continue

                for k in range(1,-2,-2):
                    new_ls = []
                    try:
                        if board[i+k][j+k] != 0  and i+k != -1 and j+k != -1:
                            board[i+k][j+k] += 1
                            if board[i+k][j+k] == 10:
                                board[i+k][j+k] = 0
                                new_ls.append((i+k,j+k))
                                flashes += flash(new_ls,flashes)
                    except:
                        continue
                for k in range(1,-2,-2):
                    new_ls = []
                    try:
                        if board[i+k][j-k] != 0  and i+k != -1 and j-k != -1:
                            board[i+k][j-k] += 1
                            if board[i+k][j-k] == 10:
                                board[i+k][j-k] = 0
                                new_ls.append((i+k,j-k))
                                flashes += flash(new_ls,flashes)
                    except:
                        continue
            return flashes

def step():
    flash_list = []
    for i in range(len(lines[0].strip())):
        for j in range(len(lines)):
            board[j][i] += 1
            if board[j][i] == 10:
                board[j][i] = 0
                flash_list.append((j,i))
    
    return flash_list

f = open("input_files/day11.in")
lines = f.readlines()
board = [[int(lines[j][i]) for i in range(len(lines[0].strip()))] for j in range(len(lines))]

for row in board:
    print(row)

flashes = 0
i = 0
while True:
    ls = step()
    flashes = flash(ls,flashes)
    # print(flashes)
    if flashes == 100:
        print(i+1)
        break
    i += 1
    # print()
    # for row in board:
    #     print(row)




# ls = step()
# flash(ls)
# print()
# for row in board:
#     print(row)

