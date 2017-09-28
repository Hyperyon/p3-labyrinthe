# -*- coding:Utf-8 -*-


def get_map():
    data = ''
    x = y = 0
    pos = []
    with open('data', 'r') as f:
        data = f.read().split('\n')

    for i, item in enumerate(data):     # need reverse read
        y = i
        for h, letter in enumerate(item):
            if letter == 'O':
                x = h
                pos.append((x, y,))

    return pos

