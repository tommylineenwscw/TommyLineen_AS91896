# This program is a simple text-based game where the player navigates through a series of rooms, collecting items and avoiding traps

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
    global lives  # Use the global variable 'lives'
    if lives > 0:  # Check if the player has lives left
        lives -= 1  # Decrease the number of lives by 1
        print(f"You lost a life! Lives remaining: {lives}")
    else:
        print("Game Over! No lives left.")
#room 1 
def room1(): 
    global lives
    print("You are in a dark room. There is a door to the north.")
    print("There is a shiny object on the ground.")
    choice = input("Do you want to pick it up? (yes/no): ").strip().lower()
    if choice == "yes":
        inventory.append("shiny object")
        print("You picked up the shiny object.")
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
def room2():
    global lives
    print("You enter a room with a treasure chest in the center.")
    print("There is a door to the south and a door to the east.")
    choice = input("Do you want to open the chest? (yes/no): ").strip().lower()
    if choice == "yes":
        print("You found a golden coin!")
        inventory.append("golden coin")
    else:
        print("You decided not to open the chest.")
    
    choice = input("Do you want to go through the south door or the east door? (south/east): ").strip().lower()
    if choice == "south":
        room1()
    elif choice == "east":
        room3()
    else:
        print("Invalid choice. You stay in the room.")   
room1() 

 