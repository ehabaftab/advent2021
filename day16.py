

def operators(data,total):
    # print(int(data[0:3],2))
    print(data)
    print()
    total += int(data[0:3],2)
    
    if int(data[3:6],2) != 4:
        
        if data[6] == '1':
            
            # print(1)
            # print()
            
            num = int(data[7:18],2)
            length = int(len(data[18:])/num)
            print(num,length)
            
            for i in range(18,18+(length*(num)),length):
                if int(data[i:i+length][3:6],2) != 4:
                    
                    total = operators(data[i:i+length],total)
                else:
                    # print(int(data[i:i+length][0:3],2))
                    total += int(data[i:i+length][0:3],2)
        else:
            print(int(data[7:22],2))
            length = int(data[7:22],2)
            if length > 11:
                for i in range(2,4):
                    if i == 3:
                        print(data[33:33+(length-11)])
                        total = operators(data[33:33+(length-11)],total)
                    else:
                        total = operators(data[11*i:(11*i)+11],total)
            else:
                try:
                    total = operators(data[22:22+length],total)
                except:
                    pass
    # else:

    
    return total

hexdata = 'C0015000016115A2E0802F182340'
binary = bin(int(hexdata,16))[2:].zfill(4*len(hexdata))
# print(binary)

final = operators(binary,0)
print(final)
