def simulate(velx,vely):
    found = True
    up_flag = True
    x = 0
    y = 0
    while y >= -260:
        found = False
        if velx != 0:
            x += velx
            velx -= 1
        if vely == -1:
            up_flag = False
            print(y)
            print(x)
            vely = 1
        if up_flag:
            y += vely
            vely -= 1
        else:
            y -= vely
            vely += 1
        if x >= 25 and x <= 67 and y >= -260 and y <= -200:
            found = True
            print('FOUND')
            return found
    


velx = 7
vely = 85

xflag = False
yflag = True
found = True

found = simulate(velx,vely)

print(velx,vely)