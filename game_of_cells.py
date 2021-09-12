import random
from copy import deepcopy as cp

class Room:
        global world, height, width

        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.cell = " "

                self.neighbours_location = []
                for i in range(-1,2):
                        for j in range(-1,2):
                                if x+i in range(0, height) and y+j in range(0, width):
                                        self.neighbours_location.append((x+i, y+j))
                self.neighbours_location.remove((x,y)) 

        def empties(self):
                empties = []
                for i,j in self.neighbours_location:
                        if world[i][j].cell == " ":
                                empties.append((i,j))
                return empties


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

def divison(x,y):
        global world, height, width

        empties = world[x][y].empties()
        if empties:
                return random.choice(empties)  

height, width = 5, 5


create_world()
insert_cells({
        "A" : [(0,0), (0,1), (1,2), (2,2)],
        #"B" : [(4,4)]seyed1378alireza
        })

show_world()

                                       
while True:
        tmp = cp(world)
        for x in range(height):
                for y in range(width):
                        if world[x][y].cell != " ":
                                ij = divison(x, y)
                                if ij:
                                        i, j = ij
                                        tmp[i][j].cell = world[x][y].cell
        world = cp(tmp)
        del tmp

        print("")
        
        show_world()



                                               
