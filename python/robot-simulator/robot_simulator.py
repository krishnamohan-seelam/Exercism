# Globals for the bearings
# Change the values as you see fit
EAST = 90
NORTH = 0
WEST = 270
SOUTH = 180


class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y =y
    
    def turn_right(self):
        self.bearing = self.bearing + 90
        if self.bearing == 360:
            self.bearing =0

    def turn_left(self):
        self.bearing = self.bearing -90
        if self.bearing == -90:
            self.bearing = 270

    def advance(self):

        if self.bearing == NORTH :
            self.y+= 1
        if self.bearing == SOUTH:
            self.y-= 1
        if self.bearing == EAST:
            self.x +=1
        if self.bearing == WEST:
            self.x -=1

    def simulate(self,commands):
        for command in commands:
            if command == 'L':
                self.turn_left()
            if command == 'R':
                self.turn_right()
            if command =='A':
                self.advance()

    @property           
    def coordinates(self):
        return self.x,self.y
        
