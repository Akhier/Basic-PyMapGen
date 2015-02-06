from Map import Map
from Rect import Rect
import random

class Map_Gen:
    def __init__(self):
        self.Width = 0
        self.Height = 0
        self.maxWall = 11
        self.minWall = 3
        self.maxHall = 7
        self.minHall = 1
        self.maxRooms = 600
        self.startRoomX = 2
        self.startRoomY = 2

    def reset(self):
        self.maxWall = 11
        self.minWall = 3
        self.maxHall = 7
        self.minHall = 1
        self.maxRooms = 600
        self.startRoomX = 2
        self.startRoomY = 2

    def gen(self, seed, width, height):
        random.seed(seed)
        self.Width = width
        self.Height = height

        Room_Count = 0
        Room_Fit = 0
        hallway = Rect()
        previous_room = Rect()
        pTiles = Map(width, height)
        outputMap = Map(width, height)
        Rooms = []

        #Starting Room Generation
        Rooms.append(Rect.create_new(self.startRoomX,
                                     self.startRoomY,
                                     random.randint(self.minWall, self.maxWall),
                                     random.randint(self.minWall, self.maxWall)))
        pTiles.set_edge(1,Rooms[Room_Count])
        outputMap.set_area(1, Rooms[Room_Count])
        Room_Count = Room_Count + 1

        #Main Room Generation
        while Room_Count < self.maxRooms:
            Room_Made = False
            BackTrack = 1
            BadRoom_Count = 1
            previous_room = Rooms[Room_Count - BackTrack]
            Rooms.append(Rect())
            while not Room_Made:
                direction = random.randint(0, 3)
                if direction == 0: #North of previous room
                    hallway = Rect.create_area(1, random.randint(self.minHall, self.maxHall))
                    hallway.set_loc(random.randint(previous_room.X, previous_room.farX()),
                                    previous_room.Y - hallway.Height)
                    Rooms[Room_Count] = Rect.create_area(random.randint(self.minWall, self.maxWall),
                                                         random.randint(self.minWall, self.maxWall))
                    Rooms[Room_Count].set_loc(hallway.X - int(Rooms[Room_Count].Width / 2),
                                              hallway.Y - Rooms[Room_Count].Height)
                elif direction == 1: #South of previous room
                    hallway = Rect.create_area(1, random.randint(self.minHall, self.maxHall))
                    hallway.set_loc(random.randint(previous_room.X, previous_room.farX()),
                                    previous_room.Y + previous_room.Height)
                    Rooms[Room_Count] = Rect.create_area(random.randint(self.minWall, self.maxWall),
                                                         random.randint(self.minWall, self.maxWall))
                    Rooms[Room_Count].set_loc(hallway.X - int(Rooms[Room_Count].Width / 2),
                                              hallway.Y + hallway.Height)
                elif direction == 2: #West of previous room
                    hallway = Rect.create_area(random.randint(self.minHall, self.maxHall), 1)
                    hallway.set_loc(previous_room.X - hallway.Width,
                                    random.randint(previous_room.Y, previous_room.farY()))
                    Rooms[Room_Count] = Rect.create_area(random.randint(self.minWall, self.maxWall),
                                                         random.randint(self.minWall, self.maxWall))
                    Rooms[Room_Count].set_loc(hallway.X - Rooms[Room_Count].Width,
                                              hallway.Y - int(Rooms[Room_Count].Height / 2))
                elif direction == 3: #East of previous room
                    hallway = Rect.create_area(random.randint(self.minHall, self.maxHall), 1)
                    hallway.set_loc(previous_room.X + previous_room.Width,
                                    random.randint(previous_room.Y, previous_room.farY()))
                    Rooms[Room_Count] = Rect.create_area(random.randint(self.minWall, self.maxWall),
                                                         random.randint(self.minWall, self.maxWall))
                    Rooms[Room_Count].set_loc(hallway.X + hallway.Width,
                                              hallway.Y - int(Rooms[Room_Count].Height / 2))

                checkPosition = True
                #Checks if the room is inside of the map border
                if Rooms[Room_Count].Y < 2:
                    checkPosition = False
                elif Rooms[Room_Count].farY() >= self.Height - 2:
                    checkPosition = False
                elif Rooms[Room_Count].X < 2:
                    checkPosition = False
                elif Rooms[Room_Count].farX() >= self.Width - 2:
                    checkPosition = False
                else:
                    #Checks each tile of the room to see if its a feature of another room
                    for y in range(Rooms[Room_Count].Height):
                        for x in range(Rooms[Room_Count].Width):
                            if pTiles.get_tile(Rooms[Room_Count].X + x, Rooms[Room_Count].Y + y) == 1:
                                checkPosition = False

                if checkPosition:
                    walldepth = 2
                    wall = Rect.create_new(Rooms[Room_Count].X - 1,
                                           Rooms[Room_Count].Y - 1,
                                           Rooms[Room_Count].Width + walldepth,
                                           Rooms[Room_Count].Height + walldepth)
                    pTiles.set_edge(1, wall)
                    outputMap.set_area(1, Rooms[Room_Count])
                    outputMap.set_area(1, hallway)
                    Room_Made = True
                    Room_Count = Room_Count + 1

                BadRoom_Count = BadRoom_Count + 1
                if BadRoom_Count >= 10:
                    BackTrack = BackTrack + 1
                    if BackTrack > Room_Count:
                        BackTrack = 1
                        Room_Fit = Room_Fit + 1

                    if Room_Fit >= 5:
                        self.maxRooms = Room_Count

        return outputMap

if __name__ == '__main__':
    test = Map_Gen()
    map = test.gen(222,75,75)
    with open('test.txt', 'w') as w:
        for y in range(map.Height):
            for x in range(map.Width):
                if map.get_tile(x, y) == 0:
                    w.write('#')
                else:
                    w.write('.')

            w.write('\n')