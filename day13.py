
# def fold(axis, k,board):
#     if axis == 'y':

#         new_board = [['.' for i in range(len(board[0]))] for j in range(k)]
#         for i in range(k):
#             for j in range(len(board[0])):
#                 if board[i][j] != '.':
#                     new_board[i][j] = board[i][j]
#                 if board[len(board)-1-i][j] != '.':
#                     # board[i][j] = board[len(board)-1-i][j]
#                     new_board[i][j] = board[len(board)-1-i][j]

#         return new_board
#     elif axis == 'x':
#         new_board = [['.' for i in range(k)] for j in range(len(board))]
#         for i in range(len(board)):
#             for j in range(k):
#                 if board[i][j] != '.':
#                     new_board[i][j] = board[i][j]
#                 if board[i][len(board[0])-1-j] != '.':
#                     # board[i][j] = board[i][len(board[0])-1-j]
#                     new_board[i][j] = board[i][len(board[0])-1-j]
#         return new_board
    


# f = open("input_files/day13.in")
# lines = f.readlines()

# max_i = 0
# max_j = 0
# for line in lines:
#     i = int(line.strip().split(',')[0])
#     j = int(line.strip().split(',')[1])
#     if i > max_i:
#         max_i = i
#     if j > max_j:
#         max_j = j

# if max_i%2 == 1:
#     max_i += 1
# if max_j%2 == 1:
#     max_j += 1

# board = [['.' for i in range(max_i+1)] for j in range(max_j+1)]



# for line in lines:
#     try:

#         i = int(line.strip().split(',')[0])
#         j = int(line.strip().split(',')[1])

#     except:
#         continue
    
#     board[j][i] = '█'
# count = 0
# for row in board:
#     for cell in row:
#         if cell == '█':
#             count += 1
# print(count)

# board = fold('x',655,board)

# board = fold('y',447,board)


# board = fold('x',327,board)

# board = fold('y',223,board)


# board = fold('x',163,board)


# board = fold('y',111,board)


# board = fold('x',81,board)


# board = fold('y',55,board)


# board = fold('x',40,board)


# board = fold('y',27,board)



# print('###############')
# board = fold('y',13,board)


# for row in board:
#     print(row)

# board = fold('y',6,board)

# print('##############')

# for row in board:
#     print(''.join(row))

# # board = fold('y',7,board)

# # count = 0
# # for row in board:
# #     for cell in row:
# #         if cell == '#':
# #             count += 1
# # for row in board:
# #     print(''.join(row))

# # board = fold('x',5,board)

# # count = 0
# # for row in board:
# #     for cell in row:
# #         if cell == '#':
# #             count += 1

# # print(count)

# # for row in board:
# #     print(''.join(row))
# #59-73, 115,125

with open('input_files/day13.in', 'r') as f:
    points, folds = f.read().split('\n\n')
    points = {tuple(map(int, p.split(','))) for p in points.split('\n')}
    folds = [(fold[11], int(fold[13:])) for fold in folds.split('\n')]

def fold_paper(points, axis, n):
    if axis == 'x':
        return {(y-(y-n)*2, x) if y > n else (y, x) for y, x in points}
    return {(y, x-(x-n)*2) if x > n else (y, x) for y, x in points}

def AOC_day13_pt1(points):
    axis, n = folds[0]
    return len(fold_paper(points, axis, n))
    
def AOC_day13_pt2(points):
    for axis, n in folds:
        points = fold_paper(points, axis, n)
    return display_code(points)

def display_code(points): 
    arr = [[' '] * 39 for _ in range(6)]
    for y, x in points:
        arr[x][y] = '#'
    return '\n'.join(''.join(row) for row in arr)

print(AOC_day13_pt1(points))
print(AOC_day13_pt2(points))