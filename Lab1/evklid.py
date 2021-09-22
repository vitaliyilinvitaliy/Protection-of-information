inp_a = int(input())
inp_b = int(input())


def Evklid(a:int, b:int):
    UVT = [[a, 1, 0],[b, 0, 1],[0, 0, 0]]

    print(UVT)

    i = 0

    while 1:
        q = int(UVT[i][0] / UVT[i + 1][0])
        UVT[i + 2][0] = UVT[i][0] % UVT[i + 1][0]
        UVT[i + 2][1] = UVT[i][1] - q * UVT[i][2]
        UVT[i + 2][2] = UVT[i + 1][1] - q * UVT[i + 1][2]

        if UVT[i + 2][0] == 0:
            break
    
        UVT.append([1,1,1])
        i = i + 1
    
    print(UVT)

    print("Answer:")
    print(UVT[i+1])


    

        

    


Evklid(inp_a, inp_b)