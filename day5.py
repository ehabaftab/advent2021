# generates all the points between two points
def generate_points(x1,y1,x2,y2):
    diff_x = x2-x1
    diff_y = y2-y1
    points = []
    if diff_x != 0 and diff_y != 0:
        interval_x = diff_x/abs(diff_x)
        interval_y = diff_y/abs(diff_y)
        for i in range(0,abs(diff_y)+1):
            points.append((int(x1 + interval_x*i),int(y1 + interval_y*i)))
    if diff_x != 0 and diff_y == 0:
        interval_x = diff_x/abs(diff_x)
        interval_y = 0
        for i in range(0,abs(diff_x)+1):
            points.append((int(x1 + interval_x*i),int(y1 + interval_y*i)))
    elif diff_y != 0 and diff_x == 0:
        interval_x = 0
        interval_y = diff_y/abs(diff_y)
        for i in range(0,abs(diff_y)+1):
            points.append((int(x1 + interval_x*i),int(y1 + interval_y*i)))
    elif diff_x == 0 and diff_y == 0:
        points.append((int(x1),int(y1)))

    return points

f = open("input_files/day5.in")
lines = f.readlines()
#lines = ["0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1", "7,0 -> 7,4", "6,4 -> 2,0","0,9 -> 2,9","3,4 -> 1,4", "0,0 -> 8,8","5,5 -> 8,2"]
board = [[0 for i in range(1000)] for j in range(1000)]

for point in lines:
    point_split = point.strip().split("->")
    x1 = int(point_split[0].split(",")[0])
    y1 = int(point_split[0].split(",")[1])
    x2 = int(point_split[1].split(",")[0])
    y2 = int(point_split[1].split(",")[1])

    # uses the generated points to increment the count of overlaps
    all_points = generate_points(x1,y1,x2,y2)
    if all_points != False:
        for coords in all_points:
            x = coords[0]
            y = coords[1]
            board[y][x] += 1

count = 0
for rows in board:
    for cells in rows:
        if cells >= 2:
            count += 1

print(count)
# for row in board:
#     print(row)
