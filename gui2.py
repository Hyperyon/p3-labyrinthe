# -*- coding:Utf-8 -*-
import pygame as pyg
import random as r


def z():
    return (r.randint(0,15)*40, r.randint(0,15)*40) #max 15

items = [z() for x in xrange(5)]


pyg.init()
fenetre = pyg.display.set_mode((600, 600))
dir = '/img/'

#loading img
fond = pyg.image.load(dir+"bg.png").convert()
perso = pyg.image.load(dir+"MG.gif").convert()
item = pyg.image.load(dir+"item.png").convert()

fenetre.blit(perso, (0,0))
pyg.display.flip()#refresh display

pos_perso = perso.get_rect()

enable = True
pyg.key.set_repeat(400, 30)


while enable:
    for event in pyg.event.get():    #waiting input key

        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                enable = False

            if event.key == pyg.K_DOWN: #if key down pressed
                pos_perso = pos_perso.move(0,40)
            if event.key == pyg.K_UP:
                pos_perso = pos_perso.move(0,-40)
            if event.key == pyg.K_LEFT:
                pos_perso = pos_perso.move(-40,0)
            if event.key == pyg.K_RIGHT:

                pos_perso = pos_perso.move(40,0)
    fenetre.blit(fond, (0,0))

    for element in items:

        fenetre.blit(item, element)
    fenetre.blit(perso, pos_perso)
    #refresh
    pyg.display.flip()


