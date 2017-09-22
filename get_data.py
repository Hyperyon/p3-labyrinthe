# -*- coding:Utf-8 -*-
dir = 'C:/Users/nico/Desktop/Nico/0Python/2017/tp/P3 - Labyrinthe/p3-labyrinthe/'

def get_map():
    data = ''
    x = y = 0
    pos = []
    with open(dir+'data', 'r') as f:
        data = f.read().split('\n')

    for i, item in enumerate(data): #need reverse read
        y = i
        for h, letter in enumerate(item):
            if letter == 'O':
                x = h
                pos.append((x,y))

    return pos
