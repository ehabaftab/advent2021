f = open("input_files/day4.in")
commands = f.readlines()


def win_check(board, numbers):
    #horizontal check check
    for i in range(5):
        if board[i][0] in numbers and board[i][1] in numbers and board[i][2] in numbers and board[i][3] in numbers and board[i][4] in numbers:
            return board,i,"horizontal",numbers[-1],numbers
        elif board[0][i] in numbers and board[1][i] in numbers and board[2][i] in numbers and board[3][i] in numbers and board[4][i] in numbers:
            return board,i,"vertical",numbers[-1],numbers
    return False
grids = []
box = [[0 for i in range(5)] for j in range(5)]
sequence = commands[0].split(',')
row = 0
column = 0
change = 0

#storing boards
for i in range(2,len(commands)):
    line = commands[i].split()
    if commands[i] != "\n":
        for j in range(len(line)):
            box[row][j] = int(line[j])
        row +=1
        change += 1
    if change == 5:
        change = 0
        row = 0
        grids.append(box)
        box = [[0 for i in range(5)] for j in range(5)]
print(len(grids))

winners = []
numbers = []
winner = False
j = 0
while winner == False:
    i = 0
    while i < len(grids):
        winner = win_check(grids[i],numbers)
        if winner != False:
            winners.append(grids[i])
            grids.pop(i)
            i = -1
        i += 1
    numbers.append(int(sequence[j]))
    j += 1

board_sum = 0
index = winner[1]
if winner[2] == "vertical":
    for i in range(5):
        for j in range(5):
            if j != index:
                if winner[0][i][j] not in winner[4]:
                    board_sum += winner[0][i][j] 
if winner[2] == "horizontal":
    for i in range(5):
        for j in range(5):
            if i != index:
                board_sum += winner[0][i][j]
print(winner[3])
print(board_sum*winner[3])
print(board_sum)
print(winners[-1])