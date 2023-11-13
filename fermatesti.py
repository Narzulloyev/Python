# Ferma Testi !!!
print('a^(n-1) mod n =>>')
n = int(input("n = "))
e = n - 1
i = bin(e)[2:]
for a in range(2,6):
    print('a=',a)
    R = a % n
    for j in range(1, len(i)):
        if i[j] == '0':
            R = (R ** 2) % n
        else:
            R = (R ** 2 * a) % n
    print(f"R[{len(i)}] = {R}")
    print(f"{a}^{e} mod {n} = {R}")
