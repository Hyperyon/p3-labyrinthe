# -*- coding:Utf-8 -*-
from msvcrt import getch
import random as r

def move_x(val):
    if not (pos[0]+val, pos[1]) in wall_pos:
        pos[0] += val

def move_y(val):
    if not (pos[0], pos[1]+val) in wall_pos:
        pos[1] += val
def z():
    return (r.randint(0,15), r.randint(0,15)) #max 15

pos = [0,0]
wall_pos = [(2,val) for val in xrange(0,5)]

keeper_pos = (15,15) #need to collect all item to pass

items = list(set([z() for x in xrange(5)])) #avoid item in same position
remaining_item = len(items)

# 77 right, 75 left, 72 top, 80 bottom
key_map = { 77:'move_x(1)',
            75:'move_x(-1)',
            72:'move_y(1)',
            80:'move_y(-1)',}

while True: #SET TRUE WHEN READY
    key = ord(getch()) #get ascii value
    if key == 27: #esc
        break

    if key != 224: #when stroke arrow key that generate 224 value
        eval(key_map[key])
        print pos

    if tuple(pos) in items:
        items.remove(tuple(pos)) #delete item when taken
        remaining_item -=1
        print 'objet trouve'
        #print items

    if tuple(pos) == keeper_pos:
        if remaining_item:
            print 'you lose'
        else:
            print 'you win !'
        break