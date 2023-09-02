# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:46:45 2023

@author: User
"""

#massiv elementlarini diagonallari bo'yicha joylashtirib chiqish kerak
# 1   3   4  10  11  21

# 2   5   9  12  20  22

# 6   8  13  19  23  30

# 7  14  18  24  29  31

#15  17  25  28  32  35

#16  26  27  33  34  36
a=0
x=[[a:=a+1 for j in range(6)] for i in range(6)]


u=0
q=0
n=1
for i in range(36):
    while u>=0 and q>=0 and u<6 and q<6:
        x[q][u]=n
        n+=1
        q+=1
        u-=1
    u+=1
    if q>5:
        u+=1
        q-=1
    while u>=0 and q>=0 and u<6 and q<6:
        x[q][u]=n
        n+=1
        q-=1
        u+=1
    q+=1
    if u>5:
        q+=1
        u-=1

for i in range(len(x)):
    for j in range(len(x[0])):
        if x[i][j]<10:
            print(x[i][j],end="    ")
        if x[i][j]>9:
            print(x[i][j],end="   ")
    print("\n")
