import random

class Cell:
        global world, height, width

        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.cell = " "


def create_world():
        global world, height, width

        world = [[Cell(x, y) for y in range(width)] for x in range(height)]

def show_world():
        global world, height, width

        for x in range(height):
                row = "["
                for y in range(width): row += world[x][y].cell
                row += "]"

                print(row)

 


height, width = 5, 5


create_world()
show_world()










