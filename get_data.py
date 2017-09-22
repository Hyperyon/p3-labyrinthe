# -*- coding:Utf-8 -*-
import random as r

dir = 'C:/Users/nico/Desktop/Nico/0Python/2017/tp/P3 - Labyrinthe/p3-labyrinthe/'
data = ''
with open(dir+'data', 'r') as f:
    data = f.read().split('\n')

x = y = 0
pos=[]
for i, item in enumerate(data[::-1]): #need reverse read
    y = i
    for h, letter in enumerate(item):
        if letter == 'O':
            x = h
            pos.append((x,y))

print pos