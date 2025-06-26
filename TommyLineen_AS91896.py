lives = 3
inventory = []

#this code is for the player to print the contents of their inventory, whenever they want to

def print_inventory():
    if inventory:
        print("You have the following items in your inventory:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")
#this code is for the player to lose a life, whenever they do something that causes them to
def lose_life():
    global lives
    if lives > 0:
        lives -= 1  
        print(f"You lost a life! Lives remaining: {lives}")
    else:
        print("Game Over! No lives left.")

def room4(): 
    global lives 
    print("\nYou enter a room with 2 small chests in the center.") 
    print("There are also 2 doors in front of you, behind these chests.") 
    
    while True:  
        print("\nOptions: open left chest, open right chest, go back, inventory")
        choice = input("What do you want to do? ").strip().lower() 
        
        if choice == "inventory":
            print_inventory() 
        
        elif choice == "open left chest":
            if "sword" not in inventory:
                print("You found a sword!")
                inventory.append("sword")
            else:
                print("The left chest is empty. You already took the sword.")  
        #the code for the player to open the right chest, but it is a mimic and attacks them 
        elif choice == "open right chest": 
            print("You opened the right chest, but it was a mimic! It attacks you!")
            lose_life() 
            if lives <= 0:
                print("Game Over! You have no lives left")
                return  
          
        elif choice == "go back":
            print("You quietly return to the dragon room to search for something useful.")
            print("As you go back through the door, the dragon is awake and very angry that it was disturbed again.")
            print("It breathes fire at you, and you lose a life.")
            lose_life()
            if lives <= 0:
                print("Game Over! You have no lives left") 
                return
            room3()  # Go back to room 3 after losing life
            return

        else:
            print("Invalid choice. Please choose a valid action.")

     
 
    

#room 3 code
def room3():
    global lives
    #what prints when the player enters room 3
    print("\nYou enter a room with an extremely large dragon asleep in the center, and it is blocking the only exit.\n")
    print("\nThere is a door to the west, but the dragon is in the way.\n")
    print("\nThere is also a door you came from to the east (back to the treasure room).\n")

     #these are the options the player has in room 3 
    while True:
        print("\nOptions: sneak, throw coin, go back, inventory")
        choice = input("What do you want to do? ").strip().lower()
        #if the player chooses inventory, it will print the contents of their inventory
        if choice == "inventory":
            print_inventory() 
        #if the player chooses to sneak, it will print that they got caught and lost a life
        elif choice == "sneak":
            print("You try to sneak past the dragon, but it wakes up and breathes fire at you!")
            lose_life() 
            #and if the player has no lives left, it will print game over.
            if lives <= 0:
                print("Game Over! You have no lives left")
                return 
        #choice to get past the room, by throwing the golden coin
        elif choice == "throw coin":
            if "golden coin" in inventory: 
                #if the player has the golden coin, it will print that they threw it and the dragon moved
                #and then it will remove the golden coin from their inventory
                print("You throw the golden coin to distract the dragon. It sleepily gets up to investigate, then clears the exit!")
                inventory.remove("golden coin")
                print("You can now escape through the west door.") 
                room4()  # Go to room 4
                break 
        #if the player chooses to go back, it will print that they returned to the treasure room
        #and then it will take them back to room 2
        elif choice in ["go back", "back"]:
            print("You quietly return to the treasure room to search for something useful.")
            room2()
            return

        #if the player chooses an invalid option, it will print that they need to choose a valid option
        else:   
            print("Invalid choice. Please choose a valid option.")
       
       
    
  #room 2 code
def room2():
    global lives
    #what prints when the player enters room 2
    print("You enter a room with a treasure chest in the center.")
    print("There is a door to the south and a door to the east.")
   #input for the player to choose whether they want to open the chest or not
    choice = input("Do you want to open the chest? (yes/no): ").strip().lower()
    #if they choose yes, it will check if they have the golden coin in their inventory 
    #and if they don't, it will add it to their inventory
    if choice == "yes":
        if "golden coin" not in inventory:
            print("You found a golden coin!")
            inventory.append("golden coin")
        else:
            print("The chest is empty. You already took the coin.")
    else:
        print("You decided not to open the chest.")
    #what happens after the player has opened the chest or not 
    #if they go through the left door, it will take them to room 1 and make a full circle. whereas if they go through the right door, it will take them to room 3
    choice = input("Do you want to go through the left door or right door? (left/right): ").strip().lower()
    if choice == "left":
        room1()
    elif choice == "right":
        room3()
    #and if the player chooses an invalid option, it will print that they need to choose a valid option
    else:
        print("Invalid choice. You stay in the room.")
#room 1 code
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

# starting the game 
room1()