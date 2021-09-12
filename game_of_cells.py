import random
from copy import deepcopy as cp
import os
import time

class Room:
        global world, height, width

        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.cell = ""

                self.neighbours_location = []
                for i in range(-1,2):
                        for j in range(-1,2):
                                if x+i in range(0, height) and y+j in range(0, width):
                                        self.neighbours_location.append((x+i, y+j))
                self.neighbours_location.remove((x,y)) 

        def empties(self):
                empties = []
                for i,j in self.neighbours_location:
                        if world[i][j].cell == "":
                                empties.append((i,j))
                return empties


def create_world(height, width, cells):

        world = [[Room(x, y) for y in range(width)] for x in range(height)]

        for cell_type in cells:
                for x,y in cells[cell_type]:
                       world[x][y].cell = cell_type

        return world

def show_world():
        global world, height, width

        for x in range(height):
                row = "["
                for y in range(width):
                        if world[x][y].cell == "":
                                row += " "
                        else: row += world[x][y].cell
                row += "]"
                print(row)

def divison(x,y):
        global world, height, width

        empties = world[x][y].empties()
        if empties:
                return random.choice(empties)  

def world_location():
        for x in range(height):
                for y in range(width):
                        yield x,y

def fight(x,y):
        fighters = []
        for i in tmp[x][y].cell:
                fighters.append(i)
        return random.choice(fighters)

                
height, width = 5, 5


world = create_world(
        height, width,
        {
                "A" : [(0,0)],
                "B" : [(4,4)]
                }
        )


show_world()

                                       
while True:
        tmp = cp(world)
        for x,y in world_location():
                if world[x][y].cell != "":
                        ij = divison(x, y)
                        if ij:
                                i, j = ij
                                tmp[i][j].cell += world[x][y].cell
        
        for x,y in world_location():
                if len(tmp[x][y].cell) > 1:
                        tmp[x][y].cell = fight(x,y)


        world = cp(tmp)
        del tmp

        print("")

        os.system('clear')  
        show_world()
        time.sleep(0.5)