import mod_lab
import prime_dig


print("Xa = ",end='')
Xa = int(input())

print("Xb = ",end='')
Xb = int(input())

def diffie_hellman():
    p = 0
    q = 0

    while 1:
        p = prime_dig.generate_prime(9999999)
        q = ((p - 1) / 2) 
        if prime_dig.isPrime(p) == True and prime_dig.isPrime(q) == True:
            q = int(q)
            break

    print("p = ", p, " q = ", q)
    print(p, " == ", (2 * q + 1))
   
    g = int(0)

    for g in range(2, p - 1):
        if mod_lab.ax_mod_p(g,q,p) != 1:
            break

    Ya = mod_lab.ax_mod_p(g, Xa, p)
    Yb = mod_lab.ax_mod_p(g, Xb, p)

    print("Ya = ", Ya)
    print("Yb = ", Yb)
    
    Zab = mod_lab.ax_mod_p(Yb, Xa, p)
    Zba = mod_lab.ax_mod_p(Ya, Xb, p)

    print("Zab = ", Zab)
    print("Zba = ", Zba)

diffie_hellman()
