# -*- coding:Utf-8 -*-
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
player = pyg.image.load(dir+"MG.gif").convert()
item = pyg.image.load(dir+"item.png").convert()
fenetre.blit(player,(0,0))
pyg.display.flip()#refresh display

my_position = player.get_rect()

print my_position

pyg.key.set_repeat(400, 30)
keyboard_input = { pyg.K_DOWN:'move_y(my_position, 40)',
                   pyg.K_UP:'move_y(my_position,-40)',
                   pyg.K_LEFT:'move_x(my_position, -40)',
                   pyg.K_RIGHT:'move_x(my_position, 40)',}

while True:
    for event in pyg.event.get(): #waiting input key
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                break
            if keyboard_input.has_key(event.key):
                my_position = eval(keyboard_input[event.key])

    fenetre.blit(background, (0,0))

    pos = (my_position[0], my_position[1])
    if pos in items:
        items.remove(pos) #delete item when taken
        remaining_item -=1

    if pos == keeper_pos:
        print pos
        if remaining_item:
            print 'you lose'
        else:
            print 'you win !'
        break

    for path in allowed_tile:
        fenetre.blit(tile, path)
    for element in items:
        fenetre.blit(item, element)

    fenetre.blit(keeper, keeper_pos)
    fenetre.blit(player, my_position)
    pyg.display.flip()
