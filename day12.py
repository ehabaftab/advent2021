def generate(point,ls,final):
    ls.append(point)
    to_go = paths[point]
    print(to_go)
    for i in range(len(to_go)):
        if to_go[i] not in ls:
            if to_go[i] == 'end':
                ls.append('end')
                final.append(ls)
                return final
            else:
                final =generate(to_go[i],ls,final)
        # return ls
    
    return final
    


f = open("input_files/day12.in")
lines = f.readlines()
paths = {}
for line in lines:
    final = line.strip().split('-')
    ls = paths.get(final[0])
    try:
        paths[final[0]] = ls + [final[1]]
    except:
        
        paths[final[0]] = [final[1]]
    ls = paths.get(final[1])
    if final[0] != 'start':
        try:
            paths[final[1]] = ls + [final[0]]
        except:
            paths[final[1]] = [final[0]]

# to_go = ['start']
# i = 0
# done = False
# while not done:
#     temp = paths[to_go[i]]
#     for j in range(len(temp)):
#         ls = [to_go[i]]
#         ls.append(temp[j])
#         print(ls)
#         to_go += paths[temp[j]]
#         print(to_go)
#     break
        
#     i += 1
#     if i >= len(to_go):
#         done = True
print(generate('start',[],[]))