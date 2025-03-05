# Location Types
MENS_RESTROOM = "men's restroom"
WOMENS_RESTROOM = "women's restroom"
CLASSROOM = "classroom"
STORAGE = "storage"
ELEVATOR = "elevator"
STUDY_ROOM = "study room"
PARKING_LOT = "parking lot"
LOBBY = "lobby"
STAIRWELL = "stairwell"
EMERGENCY_EXIT = "emergency exit"

ROOM_TYPES = [MENS_RESTROOM, WOMENS_RESTROOM, CLASSROOM, 
              STORAGE, ELEVATOR, STUDY_ROOM, PARKING_LOT, 
              LOBBY, STAIRWELL, EMERGENCY_EXIT]

# Areas
OUTSIDE_INNER = "outside inner"
OUTSIDE_OUTER = "outside outer"
BUILDING_1_LEVEL_1 = "11"
#TODO: Add the rest

class Node:
    def __init__(self, id, type, area, adjacent_nodes):
        self.area = area # ""
        self.id = id # ""
        self.type = type # ""
        
        self.adjacent_nodes = adjacent_nodes # [[Node, distance], [Node, distance]]
        