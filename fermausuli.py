#Ferma Usuli!!!
def ferma_usuli():
    n = int(input("n="))
    for q in range(1, n + 1):
        p = int((n + q**2)**0.5)
        print('q=',q,'p=',n+q**2)
        if n + q**2 == p**2:
                print(f"{n} + {q}^2 = {p}^2")
                return
    print(f"{n} soniga qo'shish orqali \
brorbir sonning kvadrati hosil bo'lmadi.")
ferma_usuli()
