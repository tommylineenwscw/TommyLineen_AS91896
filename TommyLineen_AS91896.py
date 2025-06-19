lives = 3
inventory = []

def print_inventory():
    if inventory:
        print("You have the following items in your inventory:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")

def lose_life():
    global lives
    if lives > 0:
        lives -= 1
        print(f"You lost a life! Lives remaining: {lives}")
    else:
        print("Game Over! No lives left.")

def room3():
    global lives
    print("The door locks behind you as you enter the room.")
    print("You enter a room with an extremely large dragon asleep in the center, and it is blocking the only exit.")
    print("There is a door to the west, but the dragon is in the way.")
    print("There is also a door you came from to the east (back to the treasure room).")  
      
    while True:
        print("\nOptions: sneak, throw coin, go back, inventory")
        choice = input("What do you want to do? ").strip().lower()

        if choice == "inventory":
            print_inventory() 
        elif choice == "sneak":
            print("You try to sneak past the dragon, but it wakes up and breathes fire at you!")
            lose_life()
            if lives <= 0:
                print("Game Over! You have no lives left")
                return 
        elif choice == "throw coin":
            if "golden coin" in inventory:
                print("You throw the golden coin to distract the dragon. It sleepily gets up to investigate, then clears the exit!")
                inventory.remove("golden coin")
                print("You can now escape through the west door.") 
                room4()  # Go to room 4
                break 
        elif choice in ["go back", "back"]:
            print("You quietly return to the treasure room to search for something useful.")
            room2()
            return

    choice = input("What do you want to do?").strip().lower()
    if choice == "inventory":
        print_inventory() # Show inventory
        print("You try to sneak past the dragon, but it wakes up and breathes fire at you!")
        lose_life()
        if lives <= 0:
            print("Game Over! You have no lives left")
            return
        else:
            room3()
    else:
       
        room1()  # Go back to room 1
def room2():
    global lives
    print("You enter a room with a treasure chest in the center.")
    print("There is a door to the south and a door to the east.")
    choice = input("Do you want to open the chest? (yes/no): ").strip().lower()
    if choice == "yes":
        if "golden coin" not in inventory:
            print("You found a golden coin!")
            inventory.append("golden coin")
        else:
            print("The chest is empty. You already took the coin.")
    else:
        print("You decided not to open the chest.")

    choice = input("Do you want to go through the left door or right door? (left/right): ").strip().lower()
    if choice == "left":
        room1()
    elif choice == "right":
        room3()
    else:
        print("Invalid choice. You stay in the room.")

def room1():
    global lives
    print("You are in a dark room. There is a door infront of you.")
    print("There is a shiny object on the ground.")
    choice = input("Do you want to pick it up? (yes/no): ").strip().lower()
    if choice == "yes":
        if "shiny object" not in inventory:
            inventory.append("shiny object")
            print("You picked up the shiny object.")
        else:
            print("You already picked it up.")
    else:
        print("You left the shiny object on the ground.")

    choice = input("Do you want to go through the door? (yes/no): ").strip().lower()
    if choice == "yes":
        room2()
    else:
        print("You stay in the room for a while, then get eaten by a monster that had been lurking on the wall and waiting for its chance to strike.")
        lose_life()
        if lives <= 0:
            print("Game Over! You have no lives left.")
            return
        else:
            room1()

# Start the game
room1()