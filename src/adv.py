from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# print(dir())

# Make a new player object that is currently in the 'outside' room.
from player import Player
player1 = Player("player1", room['outside'])

# print(room['outside'].n_to[0])
# print(player1.location)
# Write a loop that:

play_game = True
while play_game == True:
#
# * Prints the current room name
    print(f"your location is {player1.location.name}")
# * Prints the current description (the textwrap module might be useful here).
#    room_in = room.get(player1.location)
    room_in = player1.location
    print(room_in.description)
# * Waits for user input and decides what to do.
    print("Where would you like to go?")
    direction = input("[n] North [s] South [e] East [w] West [q] quit\n")

#Valid commands are n, s, e and w which move the player North, South, East or West
    # print(direction)
    if direction == "n" or direction == "s" or direction == "e" or direction == "w" direction == "q":
        if direction == "n":
            room_in = player1.location.n_to
        if direction == "s":
            room_in = player1.location.s_to
        if direction == "e":
            room_in = player1.location.e_to
        if direction == "w":
            room_in = player1.location.w_to
        if direction == "q":
            play_game = False
    else:
        print("Per MVP only n, s, e and w are valid commands, NO OTHER SOLUTIONS ARE VALID")

    player1.location = room_in
    print()


#
# If the user enters a cardinal direction, attempt to move to the room there.
#    print(direction)
"""
    try:
        try:
            if int(direction) == 1:
                room_in = player1.location.n_to
            if int(direction) == 2:
                room_in = player1.location.s_to
            if int(direction) == 3:
                room_in = player1.location.e_to
            if int(direction) == 4:
                room_in = player1.location.w_to
            if int(direction) == 5:
                play_game = False
        except ValueError:
            print("Please pick a valid choice [1 to 5]")
"""
#    if int(direction) == 1:
#        room_in = room[player1.location].n_to
#        player1.location = room_in.name
#        print(player1.location)
# Print an error message if the movement isn't allowed.
"""
    except AttributeError:
        if int(direction) == 1:
            print("North is not a vaalid direction")
        if int(direction) == 2:
            print("South is not a vaalid direction")
        if int(direction) == 3:
            print("East is not a vaalid direction")
        if int(direction) == 4:
            print("West is not a vaalid direction")
    player1.location = room_in # needs to be the KEY not "name"
    print()
"""
#    print(player1.location)
#
# If the user enters "q", quit the game.
    # x = False
