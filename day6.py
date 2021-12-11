

f = open("input_files/day6.in")
initial = f.readlines()
fish = initial[0].split(",")
ls = []
for f in fish:
    ls.append(int(f))

mem = {}
training = [1,2,3,4,5,6,7,8]
for inputs in training:
    train_ls = [inputs]
    i = 0
    while i < 256:
        j = 0
        count = len(train_ls)
        while j < count:
            train_ls[j] -= 1
            if train_ls[j] == -1:
                train_ls = train_ls + [8]
                train_ls[j] = 6
            j += 1
        i += 1
    mem[inputs] = train_ls

new_ls = []
j = 0
while j < len(ls):
    for i in range(1,9):
        if ls[j] == i:
            new_ls = new_ls + mem[i] 
    j += 1


print(len(new_ls))




# def day(ls,n):

#     if n == 80:
#         return ls

#     j = 0
#     count = len(ls)
#     while j < count:
#         ls[j] -= 1
#         if ls[j] == -1:
#             ls = ls + [8]
#             ls[j] = 6
#         j += 1
#     return day(ls,n+1)


# print(day(ls,0))