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

from items import Items

# Items

items = {
    'gold': Items("Gold", "is shiny"),
    'lamp': Items("Lamp", "has a blue light"),
}

room['outside'].item_list.append(items['gold'])

#
# Main
#
# print(dir())

# Make a new player object that is currently in the 'outside' room.
from player import Player
player1 = Player("player1", room['outside'])
# Player inventory
player1.item_list.append(items['lamp'])

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
    for i in room_in.item_list:
        print(f"you see {i.item_name}")
    for i in player1.item_list:
        print(f"your {i.item_name} {i.description}")
    # print(room_in.w_to)
# * Waits for user input and decides what to do.
    print("Where would you like to go?")
    direction = input("[n] North [s] South [e] East [w] West [i] inventory [q] quit\n *Hint you can take or drop an item\n")
    if direction.split()[0] == "take" or direction.split()[0] == "get":
        # print("would take")
        for i in room_in.item_list:
            if i.item_name == direction.split()[1]:
                player1.item_list.append(items[direction.split()[1].lower()])
                room_in.give_error = False
        room_in.get_item(direction.split()[1])
        if room_in.give_error == True:
            print("An item must be here to take it")
    if direction.split()[0] == "drop":
        #print("would drop")
        for i in player1.item_list:
            if i.item_name == direction.split()[1]:
                room_in.item_list.append(items[direction.split()[1].lower()])
                player1.give_error = False
        player1.get_item(direction.split()[1])
        if player1.give_error == True:
            print("You must have an item to drop it")
    else:
#Valid commands are n, s, e and w which move the player North, South, East or West
    # print(direction)
    #    if direction == "i" or direction == "inventory" or direction == "n" or direction == "s" or direction == "e" or direction == "w" or direction == "q":
        if direction == "n":
            if player1.location.n_to == "none":
                print("pick a valid direction")
            else:
                room_in = player1.location.n_to
        if direction == "s":
            if player1.location.s_to == "none":
                print("pick a valid direction")
            else:
                room_in = player1.location.s_to
        if direction == "e":
            if player1.location.e_to == "none":
                print("pick a valid direction")
            else:
                room_in = player1.location.e_to
        if direction == "w":
            if player1.location.w_to == "none":
                print("pick a valid direction")
            else:
                room_in = player1.location.w_to
        if direction == "i" or direction == "inventory":
            print("In your inventory you have:")
            for i in player1.item_list:
                print(f"your {i.item_name} it {i.description}")
        if direction == "q":
            play_game = False
        else:
            print("Valid directions n, s, e and w")

    player1.location = room_in
    print()

    player1.give_error = True
    room_in.give_error = True


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
