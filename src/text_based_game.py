
"""
Project Two: Haunted Mansion Text Adventure Game
Author: Robert Harris
"""

def show_instructions():
    """Display the game objective and available commands."""
    print("\nWelcome to the Haunted Mansion!")
    print("Collect all 6 items before entering Ghost's Chamber.")
    print("If you enter Ghost's Chamber too early, you lose!")
    print("\nCommands:")
    print("  go north")
    print("  go south")
    print("  go east")
    print("  go west")
    print("  get item name")
    print("Example: get candle")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("\nYou are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])


def main():
    """Run the main gameplay loop."""

    # Store each room, its connections, and its item.
    rooms = {
        "Foyer": {
            "north": "Ballroom",
            "south": "Kitchen",
            "east": "Library",
            "west": "Bedroom"
        },
        "Bedroom": {
            "east": "Foyer",
            "north": "Attic",
            "item": "old key"
        },
        "Attic": {
            "south": "Bedroom",
            "item": "candle"
        },
        "Library": {
            "west": "Foyer",
            "north": "Basement",
            "item": "spell book"
        },
        "Basement": {
            "south": "Library",
            "item": "amulet"
        },
        "Kitchen": {
            "north": "Foyer",
            "east": "Dining Room",
            "item": "potion"
        },
        "Dining Room": {
            "west": "Kitchen",
            "north": "Ballroom",
            "item": "silver knife"
        },
        "Ballroom": {
            "south": "Foyer",
            "west": "Dining Room",
            "east": "Ghost's Chamber"
        },
        "Ghost's Chamber": {
            "west": "Ballroom"
        }
    }

    # Set the player's starting room and inventory.
    current_room = "Foyer"
    inventory = []
    total_items = 6

    # Display the game instructions.
    show_instructions()

    # Continue playing until the player wins or loses.
    while True:
        # Check whether the player entered the villain's room.
        if current_room == "Ghost's Chamber":
            if len(inventory) == total_items:
                print("\nCongratulations! You collected all 6 items!")
                print("You defeated the ghost and won the game!")
            else:
                print("\nOh no! The ghost caught you!")
                print("GAME OVER! You did not collect all 6 items.")
            break

        # Display the player's status.
        show_status(current_room, inventory, rooms)

        # Ask the player for the next command.
        command = input("\nEnter your move: ").strip().lower()

        # Handle movement commands.
        if command.startswith("go "):
            direction = command[3:]

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You cannot go that way!")

        # Handle item collection commands.
        elif command.startswith("get "):
            item_name = command[4:].strip()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if item_name == room_item.lower():
                    inventory.append(room_item)
                    print("You collected the", room_item + "!")
                    del rooms[current_room]["item"]
                else:
                    print("That item is not in this room.")
            else:
                print("There is no item to collect in this room.")

        # Handle invalid commands.
        else:
            print("Invalid command. Try 'go north' or 'get candle'.")

    print("\nThanks for playing the Haunted Mansion!")
    print("Hope you enjoyed the game.")


if __name__ == "__main__":
    main()
