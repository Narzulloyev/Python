# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 08:51:50 2023

@author: User
"""

n=1
x=[[(n:=n+1) if n==0 else (n:=n-1) for x in range(5)] for i in range(5)]

for i in range(len(x)):
    for j in range(len(x[i])):
        if x[i][j] > 9:
            print(x[i][j], end="   ")
        else:
            print(x[i][j] , end="    ")
    print('\n')