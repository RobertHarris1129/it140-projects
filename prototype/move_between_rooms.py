"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}



# Set the player's starting room.
current_room = 'Great Hall'

# Gameplay loop.
while current_room != 'exit':
    print('\nYou are in the', current_room)

    command = input('Enter a move (go north, go south, go east, go west) or exit: ').lower().strip()

    if command == 'exit':
        current_room = 'exit'

    elif command.startswith('go '):
        direction = command[3:]

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print('You cannot go that way!')

    else:
        print('Invalid command. Please try again.')

print('Thanks for playing!')
