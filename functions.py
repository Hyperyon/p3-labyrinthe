# -*- coding:Utf-8 -*-
import pygame as pyg
import random as r
import get_data as data

dir = 'absolute_path_dir/img/'


class Object:
    '''This class manage the behaviour of each item in the game'''
    pyg.init()
    window = pyg.display.set_mode((600, 600))
    allowed_tile = [(x[0]*40, x[1]*40) for x in data.get_map()]
    items = [(x[0], x[1],) for x in r.sample(allowed_tile, 5,)]
    font = pyg.font.Font(None, 40)
    text = font.render(str(len(items)), 1, (10, 10, 10,))
    textpos = text.get_rect()

    def __init__(self, entity):
        temp = pyg.image.load(dir+entity+".png").convert()
        setattr(self, entity, temp)

    def move_x(self, pos, x):
        if not (pos[0] + x, pos[1],) in self.allowed_tile:
            x = 0
        return pos.move(x, 0,)

    def move_y(self, pos, y):
        if not (pos[0], pos[1] + y,) in self.allowed_tile:
            y = 0
        return pos.move(0, y,)

    def get_position(self):
        return self.player.get_rect()

    def refresh(self):
        pyg.display.flip()

    def repeat_key(self):
        pyg.key.set_repeat(400, 30)

keyboard_input = {pyg.K_DOWN:'player.move_y(my_position, 40)', 
                  pyg.K_UP:'player.move_y(my_position,-40)', 
                  pyg.K_LEFT:'player.move_x(my_position, -40)', 
                  pyg.K_RIGHT:'player.move_x(my_position, 40)',}


def start_game():
    player = Object('player')
    background = Object("bg")
    tile = Object("tile")
    keeper = Object("keeper")
    item = Object("item")

    remaining_item = len(player.items)
    keeper_pos = (14*40, 14*40)

    player.window.blit(player.player, (0, 0,))
    player.refresh()
    my_position = player.get_position()

    player.repeat_key()

    enable = True
    while enable:
        for event in pyg.event.get():       # waiting input key
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        enable = False
                    if event.key in keyboard_input:
                        my_position = eval(keyboard_input[event.key])

        player.window.blit(background.bg, (0, 0,))

        pos = (my_position[0], my_position[1])
        if pos in player.items:
            player.items.remove(pos)        # delete item when taken
            remaining_item -= 1

        if pos == keeper_pos:
            print(pos)
            if remaining_item:
                print('you lose')
            else:
                print('you win !')
            break

        for path in player.allowed_tile:
            player.window.blit(tile.tile, path)
        for element in player.items:
            player.window.blit(item.item, element)

        text = player.font.render(str(remaining_item), 1, (10, 10, 10,))
        player.window.blit(text, player.textpos)

        player.window.blit(keeper.keeper, keeper_pos)
        player.window.blit(player.player, my_position)
player.refresh()
