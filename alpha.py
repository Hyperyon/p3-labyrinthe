# -*- coding:Utf-8 -*-
from msvcrt import getch
import random as r

def z():
    return (r.randint(0,15), r.randint(0,15)) #max 15


items = list(set([z() for x in xrange(5)])) #avoid item in same position
#print items

pos = (0,0)
keeper_pos = (15,15) #need to collect all item to pass
x = 0
y = 0
remaining_item = len(items)

wall_pos = [(2,val) for val in xrange(0,5)]

print wall_pos
while True:
    key = ord(getch()) #get ascii value

    if key == 27: #esc
        break

    if key == 72 and y < 15: #haut
        y+=1
        print 'haut'

    elif key == 80 and y > 0:
        y-=1
        print 'bas'

    elif key == 75 and x > 0:
        x-=1
        if pos in wall_pos:
            x+=1
        print 'gauche'

    elif key == 77 and x < 15:
        x+=1
        if pos in wall_pos:
            x-=1
        print 'droite'

    if key != 224:
        pos = (x,y)
        print pos

        if pos in items:
            items.remove(pos) #delete item when taken
            remaining_item -=1
            print 'objet trouve'
            #print items

        if pos == keeper_pos:
            if remaining_item:
                print 'you lose'
            else:
                print 'you win !'
            break