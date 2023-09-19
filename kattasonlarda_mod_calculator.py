a = int(input("Bo'linuvchi son a = "))
e = int(input("Bolinuvchining darajasi e = "))
n = int(input("Bo'luvchi son n = "))
i = bin(e)[2:]
R = a % n

for j in range(1, len(i)):
    print(f"R[{j - 1}] = {R}")
    if i[j] == '0':
        R = (R ** 2) % n
    else:
        R = (R ** 2 * a) % n

print(f"R[{len(i)}] = {R}")
