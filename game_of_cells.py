import random
from copy import deepcopy as cp
import os
import time
from colorama import Fore #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

class Room:
        global world, height, width

        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.cell = ""
                self.neighbours_location = self.create_neighbours_location()

        def empties(self):
                empties = []
                for i,j in self.neighbours_location:
                        if world[i][j].cell == "":
                                empties.append((i,j))
                return empties
        
        def create_neighbours_location(self):
                neighbours_location = []

                for i in range(-1,2):
                        for j in range(-1,2):
                                if self.x+i in range(0, height) and self.y+j in range(0, width):
                                        neighbours_location.append((self.x+i, self.y+j))
                neighbours_location.remove((self.x,self.y))
                return neighbours_location

        def divison_state(self):
                if self.cell != "":
                        if self.empties():
                                return True
                return False
                
        def competition_state(self):
                if len(tmp[self.x][self.y].cell) > 1:
                        return True
                return False
                
        def divison(self):
                empties = self.empties()
                return random.choice(empties)
        
        def competition(self):
                fighters = []
                for i in self.cell:
                        fighters.append(i)
                return random.choice(fighters)
                        
def create_world(height, width, types, locations):

        world = [[Room(x, y) for y in range(width)] for x in range(height)]
        for cell_type in types:
                for x,y in locations[cell_type]:
                       world[x][y].cell = cell_type
        return world

def show_world():
        global world, height, width

        for x in range(height):
                row = Fore.RESET+"["
                for y in range(width):
                        cell_type =  world[x][y].cell
                        if cell_type == "": cell_type = " "
                        row += cell_colors[cell_type] + cell_type
                row += Fore.RESET+"]"
                print(row)

def world_location():
        for x in range(height):
                for y in range(width):
                        yield x,y


                
height, width = 5, 5
cell_types = ["A", "B", "C"]
cell_locations = {
        "A": [(0,0)],
        "B": [(4,4)],
        "C": [(2,4)]    
}
cell_colors = {
        "A": Fore.GREEN,
        "B": Fore.RED,
        "C": Fore.BLUE,
        " ": Fore.RESET       
}

world = create_world(height, width, cell_types, cell_locations)

show_world()

flag = True                                
while flag:
        flag = False
        tmp = cp(world)
        for x,y in world_location():
                if world[x][y].divison_state():
                        cell_type = world[x][y].cell
                        r, c = world[x][y].divison()

                        tmp[r][c].cell += cell_type

                        if tmp[r][c].competition_state():
                                winner = tmp[r][c].competition()
                                tmp[r][c].cell = winner
                        
                        flag =  True

        world = cp(tmp)  
        del tmp
        os.system('clear')  
        show_world()
        time.sleep(0.05)