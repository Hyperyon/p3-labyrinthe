# -*- coding: utf-8 -*-

import random as r
import pygame as pyg

DIR = 'img/'

keyboard_input = {pyg.K_DOWN: 'player.move_y(40)',
                  pyg.K_UP: 'player.move_y(-40)',
                  pyg.K_LEFT: 'player.move_x(-40)',
                  pyg.K_RIGHT: 'player.move_x(40)',}


class UserInterface:

    ''' Manage graphical user interface. '''

    # main elements used by interface
    ELEMENTS = ['player', 'wall_background', 'tile', 'keeper', 'item']

    def __init__(self):
        pyg.init()
        # make a window 600 by 600 pixel
        self.window = pyg.display.set_mode((600, 600))
        self.font = pyg.font.Font(None, 40)
        self.load_element()

        self.position = self.player.get_rect()
        self.keeper_position = (14*40, 14*40)

        my_maze = Maze()
        self.allowed_tiles = my_maze.get_map()

        # generate 3 random object coordinates
        self.objects = [position for position in r.sample(self.allowed_tiles, 3)]

    def load_element(self):
        '''Loading all sprites'''
        for item in UserInterface.ELEMENTS:
            setattr(self, item, pyg.image.load(DIR + item + ".png").convert())

    def show_text(self, message):
        '''Show remaining item on the top left'''
        self.text = self.font.render((str(message)), 1, (10, 10, 10))
        self.textpos = self.text.get_rect()
        self.window.blit(self.text, self.textpos)

    def show_element(self):
        '''
        Element showed in this order :
        background, tiles, object, text, McGyver and keeper
        '''
        self.window.blit(self.wall_background, (0, 0))
        # show the maze path
        for tile in self.allowed_tiles:
            self.window.blit(self.tile, tile)
        # show  item that will be taken by player
        for item in self.objects:
            self.window.blit(self.item, item)

        self.show_text(str(len(self.objects)))
        self.window.blit(self.player, self.position)
        self.window.blit(self.keeper, self.keeper_position)

    def refresh(self):
        '''Clean all graphics elements'''
        pyg.display.flip()

    def repeat_key(self):
        '''
        Move few times character when key pressed for a long time
        '''
        pyg.key.set_repeat(400, 30)



class GamePlay:

    """ Manage mechanisms of game. """

    def __init__(self, player):
        self.player = player

    def move_x(self, x):
        '''Manage horizontal moves'''
        # check next coordinates if are allowed
        next_position = self.player.position[0] + x, self.player.position[1]
        if not next_position in self.player.allowed_tiles:
            # if not, player not move
            x = 0
        self.player.position = self.player.position.move(x, 0)

    def move_y(self, y):
        '''Manage vertical moves'''
        next_position = self.player.position[0], self.player.position[1] + y
        if not next_position in self.player.allowed_tiles:
            y = 0
        self.player.position = self.player.position.move(0, y)

    def check_objects(self):
        '''When player is next to a chest, that remove item on UI'''
        pos = (self.player.position[0], self.player.position[1])

        # compare player position with objects
        if pos in self.player.objects:
            # delete item when taken
            self.player.objects.remove(pos)

        # compare player position with keeper position
        if pos == self.player.keeper_position:
            self.check_end_game()
            # end game
            return False

        # continue game
        return True

    def check_end_game(self):
        '''When player is next to keeper,
        that check if player have all items
        '''
        if self.player.objects:
            print('you loose')
        else:
            print('you win')


class Maze:

    """ Read data file to generate maze. """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.ok_tiles_positions = []

    def read_data_file(self):
        '''Get level of labyrinth from data file'''
        with open('data', 'r') as my_file:
            data = my_file.read().split('\n')
            return data
        # if fail to read file
        return False

    def get_map(self):
        '''Convert data file into list of coordinates'''
        data = self.read_data_file()

        if data:
            for ordinate, item in enumerate(data):
                self.y = ordinate
                for abscisse, letter in enumerate(item):
                    if letter == 'O':
                        self.x = abscisse
                        self.ok_tiles_positions.append((self.x*40, self.y*40))
            return self.ok_tiles_positions


def start_game():

    '''Instanciate class
    and awaiting user keybord input from player
    '''

    interface = UserInterface()
    player = GamePlay(interface)
    interface.repeat_key()
    continue_game = True

    while 'user playing' and continue_game:

        for event in pyg.event.get():
            # waiting input key from user
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    # end game when pressed escape key
                    continue_game = False
                if event.key in keyboard_input:
                    eval(keyboard_input[event.key])

        interface.show_element()
        if not player.check_objects():
            # when player is next to the keeper, the game ends
            break
        interface.refresh()
