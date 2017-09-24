# -*- coding:Utf-8 -*-
'''This is >>procedural<< version of game'''

import pygame as pyg
import random as r
import get_data as data

dir = 'C:/Users/nico/Desktop/Nico/0Python/2017/tp/P3 - Labyrinthe/p3-labyrinthe/img/'

allowed_tile = [(x[0]*40, x[1]*40) for x in data.get_map()]
items = [(x[0], x[1]) for x in r.sample(allowed_tile,5)]
remaining_item = len(items)
keeper_pos = (14*40,14*40)

def move_x(pos, x):
    if not (pos[0]+x,pos[1]) in allowed_tile:
        x=0
    return pos.move(x,0)

def move_y(pos, y):
    if not (pos[0],pos[1]+y) in allowed_tile:
        y=0
    return pos.move(0,y)

pyg.init()
fenetre = pyg.display.set_mode((600, 600))

#loading img
background = pyg.image.load(dir+"bg.png").convert()
tile = pyg.image.load(dir+"tile.png").convert()
keeper = pyg.image.load(dir+"keeper.png").convert()
player = pyg.image.load(dir+"player.png").convert()
item = pyg.image.load(dir+"item.png").convert()

font = pyg.font.Font(None, 40)
text = font.render(str(remaining_item), 1, (10,10,10))
textpos = text.get_rect()

fenetre.blit(player,(0,0))
pyg.display.flip()#refresh display

my_position = player.get_rect()

pyg.key.set_repeat(400, 30)
keyboard_input = { pyg.K_DOWN:'move_y(my_position, 40)',
                   pyg.K_UP:'move_y(my_position,-40)',
                   pyg.K_LEFT:'move_x(my_position, -40)',
                   pyg.K_RIGHT:'move_x(my_position, 40)',}

enable = True

while enable:
    for event in pyg.event.get(): #waiting input key
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                enable = False
            if event.key in keyboard_input:
                my_position = eval(keyboard_input[event.key])

    fenetre.blit(background, (0,0))

    pos = (my_position[0], my_position[1])
    if pos in items:
        items.remove(pos) #delete item when taken
        remaining_item -=1

    if pos == keeper_pos:
        print pos
        if remaining_item:
            print('you lose')
        else:
            print('you win !')
        break

    for path in allowed_tile:
        fenetre.blit(tile, path)
    for element in items:
        fenetre.blit(item, element)

    text = font.render(str(remaining_item), 1, (10,10,10))
    fenetre.blit(text, textpos)
    fenetre.blit(keeper, keeper_pos)
    fenetre.blit(player, my_position)

    pyg.display.flip()
