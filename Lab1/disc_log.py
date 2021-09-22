import mod_lab

print("Input a: ", end="")
a = int(input())

print("Input p: ", end="")
p = int(input())

print("Input y: ", end="")
y = int(input())

def discrete_logarithm(a :int, p :int, y:int):
    m = k = int(p ** 0.5) + 1
    print("m = ", m, " k = ", k)

    list1 = []
    list2 = []

    for i in range(0, m + 1):
        list1.append((y * (a ** i)) % p)
    
    x = int(0)

    for i in range(1, k):
        power = m * i
        elem = (a ** power) % p
        list2.append(elem)

        if elem in list1:
            x = i * m - list1.index(elem)
            print("x = ", x)
            print("checking - ", mod_lab.ax_mod_p(a,x,p), " = ", y)
            break

    print(list1)
    print(list2)
    

discrete_logarithm(a, p, y)
