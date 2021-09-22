
#print("Input a: ", end='')
#inp_a = int(input())

#print("Input x: ", end='')
#inp_x = int(input())

#print("Input p: ", end='')
#inp_p = int(input())

def ax_mod_p(a :int, x:int, p:int):

#    print(a, '^', x, ' mod ', p, sep='')

    binary_x = ''
    binary_x = bin(x)

#    print(x, binary_x, sep=' = ')

    len_binary_x = len(binary_x) - 2
#    print('log2[', x, '] + 1 = ', len_binary_x)

    mas = []

    mas.append(a)
#    print('mas[0] = ', mas[0])
    
    for i in range(1, len_binary_x):
        mas.append((mas[i - 1]**2)%p)
#        print('mas[', i,'] = ', mas[i])

    res = 1
    index_mass = 0

    for i in range(len(binary_x) - 1, 1, -1):
        if(binary_x[i] == '1'):
            res = res * mas[index_mass]
        index_mass = index_mass + 1

    res = res % p
    return res
    #print('res = ', res)
    
#ax_mod_p(inp_a, inp_x, inp_p)
