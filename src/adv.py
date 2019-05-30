from room import Room
from player import Player
from item import Item

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

# Make a new player object that is currently in the 'outside' room.
player = Player("Davina", room["outside"].name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
def room_current():
  for i in room:
    if player.current_room == room[i].name:
      print(room[i].name)
      print(room[i].description)
      for x in room[i].items:
        print(f"\nYou see a {x.name}: {x.description}")
      return room[i]

def moveLoop(current_room, move):
  moving = move + "_to"
  room_next = getattr(current_room, moving)
  player.current_room = room_next.name
  print("Invalid Entry")
  return player

def start():
  while True:
    location_start = room_current()
    cmd = input("\n Choose a direction: [n] North, [e] East, [s] South, [w] West, Actions: [p] Pickup Item [d], Drop Item, Quit: [q] End Game ").split()
    one_cmd = cmd[0]
    two_cmd = cmd[-1]
    if cmd == "q":
      print("Game over!")
      break

    elif cmd == "n" or cmd == "e" or cmd == "s" or cmd == "w":
      try:
        moveLoop(location_start, cmd)
      except AttributeError:
        print("Cannot go that direction")

    elif one_cmd == "p":
      try:
        for x in room:
          room_items = room[x].items
          for y in room_items:
            if i.name == two_cmd:
              player.inventory.append(i.name)
              room_item.remove(i)
              print(f"\n You have picked the {i.name}")
              break
            else:
              print("Cannot find that item in this room")

    elif one_cmd == "d":
      player_items = player.inventory
      for z in player_items:
        if z == two_cmd:
          player.inventory.remove(z)
          print(f"\n You dropped the {z}")
          break
        else:
          print("\n You are not holding that item")
    else:
      print("Invalid Command")

start()
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
