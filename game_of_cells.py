import random

class Room:
        global world, height, width

        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.cell = " "


def create_world():
        global world, height, width

        world = [[Room(x, y) for y in range(width)] for x in range(height)]

def show_world():
        global world, height, width

        for x in range(height):
                row = "["
                for y in range(width): row += world[x][y].cell
                row += "]"

                print(row)

def insert_cells(cells):
        global world, height, width

        for cell_type in cells:
                for x,y in cells[cell_type]:
                       world[x][y].cell = cell_type  


height, width = 5, 5


create_world()
insert_cells({
        "A" : [(0,0), (0,1), (1,2), (2,2)],
        #"B" : [(4,4)]
        })

show_world()