print("Welcome to the Game!")
print("You will explore a dungeon filled with treasures, traps, and monsters.") 
print("PRIVACY NOTICE: This game is for educational purposes only and does not collect any personal data.")
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


#this code is for room 5, which is a dead end room that kills the player
def room5(): 
    print("\n You enter a mysterious room with nothing in it.") 
    print("as you try to leave, the door slams shut behind you!") 
    print("The walls start to close in on you, and you realize you are trapped!") 
    print("\n You get crushed by the walls and die!") 
    print("Game over.")
    

#this code is for the pit room, which is a room that the player can fall into and get trapped in
def pitroom(): 
    print("\nAs you enter the room, it is pitch black and you can't see anything. You hear a faint dripping sound.") 
    print("\nSuddenly, the floor gives way beneath you and you fall into a deep pit!")
    print("You land softly on a pile of treasure, but you are trapped in the pit") 
    print("\nYou can hear extremely loud growling and scratching noises coming from above, and you know you are screwed.") 
    print("\nYou can try to climb out, but it is too slippery and you keep falling back down.") 
    print("\n Suddenly, you realize what is making the noises. The Dragon from the previous room has followed you into the pit and jumps down after you!") 
    #options for the player to choose from, to try and escape the pit
    print("1. try to find a weapon in your bag") 
    print("2. try to climb on top of the dragon and tame it") 
    print("3. throw the shiny object at the dragon")
    choice = input("What do you want to do? (1/2/3): ").strip() 
    #if the player chooses to find a weapon, it will check if they have a sword in their inventory
    #and if they do, it will print that they fought the dragon and won, but they are still trapped in the pit
    if choice == "1":
      if "sword" in inventory:
        print("\nYou quickly draw your sword and fight the dragon!")
        print("After a fierce battle, you manage to slay the dragon, but you are still trapped in the pit.") 
        print("game over.") 
        #however, if the player does not have a sword, it will print that they have no weapon to defend themselves with and they will die.
    else:
        print("\nYou have no weapon to defend yourself with!")
        print("The dragon attacks you and incinerates you with its fiery breath!")
        print("game over.") 
        #If the player chooses to climb on top of the dragon, it will check if they have a shiny object in their inventory
        #and if they do, it will print that they tamed the dragon and escaped the dungeon
    if choice == "2": 
        if "shiny object" in inventory:
            print("\nYou climb onto the dragon's back and try to tame it with the shiny object.")
            print("The dragon is mesmerized by the shiny object and allows you to ride it of the pit.") 
            print("it then burst through the ceiling and you see the light of day again! You have escaped the dungeon!") 
            print("You Win!") 
            #if they don't, they will die.
        else:
            print("\nYou try to climb onto the dragon, but it throws you off and you fall back into the pit!")
            print("The dragon then attacks you and incinerates you with its fiery breath!")
            print("Game over.") 
            
        #you die either way if you choose this option, but it will print different messages depending on whether you have the shiny object or not.
        #if you do:
    if choice == "3":
    
        if "shiny object" in inventory:
            print("\nYou throw the shiny object at the dragon, distracting it momentarily.")
            print("It then looks at you and roars in anger, and incinerates you with its fiery breath!") 
            print ("Game over.") 
            #if you don't:
        else:
            print("\nYou try to throw a shiny looking rock on the ground at the dragon, but it doesn't care and attacks you!")
            print("The dragon incinerates you with its fiery breath!")
            print("Game over.")

#room 4 code
def room4():
    global inventory, lives

    print("\nYou enter a room with two mysterious chests: one on the left and one on the right.")
    print("There are also doors to the left and right.")

    chest_opened = False
    # Loop until the player has opened one of the chests
    while not chest_opened:
        print("\nWhat do you want to do?")
        print("1. Open the left chest")
        print("2. Open the right chest")
        print("3. Go right")
        print("4. Go left")
        print("5. Check inventory")

        choice = input("> ")
        #choice if player opens the left chest
        if choice == "1":
            print("\nYou open the left chest and find a gleaming sword!")
            inventory.append("sword")
            chest_opened = True
        #what happens if the player opens the right chest
        elif choice == "2":
            print("\nAs you open the right chest, it suddenly grows teeth and lunges at you!")
            print("It's a mimic! You manage to fight it off, but it bites you. You lose a life.")
            lives -= 1
            print(f"Lives remaining: {lives}")
            chest_opened = True 
            #if the player wants to go past the chests, it will print that they should check them first
        elif choice == "3" or choice == "4":
            print("\nMaybe you should check out the chests first...")
        elif choice == "5":
            print_inventory()
        else:
            print("\nInvalid choice. Please try again.")

    # After chest interaction
    while True:
        print("\nWhich door do you want to go through?")
        print("1. right door")
        print("2. left door")

        direction = input("> ")

        if direction == "1":
            print("\nYou go through the door to the right.")
            room5()
            break
        elif direction == "2":
            print("\nYou go through the door to the left.")
            pitroom()
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

     
 
    

#room 3 code
def room3():
    global lives
    #what prints when the player enters room 3
    print("\nYou enter a room with an extremely large dragon asleep in the center, and it is blocking the only exit.")
    print("There is a door in front of you, but the dragon is in the way.")
    print("There is also a door you came from (back to the treasure room).\n")

     #these are the options the player has in room 3 
    while True: 
        print("\n options:") 
        print("1. sneak past the dragon")
        print("2. throw the golden coin at the dragon") 
        print("3. go back to the treasure room")
        print("4. check inventory")
        
        choice = input("What do you want to do? (1/2/3/4) ").strip().lower()
        #if the player chooses inventory, it will print the contents of their inventory
        if choice == "4":
            print_inventory() 
        #if the player chooses to sneak, it will print that they got caught and lost a life
        elif choice == "1":
            print("You try to sneak past the dragon, but it wakes up and breathes fire at you!")
            lose_life() 
            #and if the player has no lives left, it will print game over.
            if lives <= 0:
                print("Game Over! You have no lives left")
                return 
        #choice to get past the room, by throwing the golden coin
        elif choice == "2":
            if "golden coin" in inventory: 
                #if the player has the golden coin, it will print that they threw it and the dragon moved
                #and then it will remove the golden coin from their inventory
                print("You throw the golden coin to distract the dragon. It sleepily gets up to investigate, then clears the exit!")
                inventory.remove("golden coin")
                print("You can now escape through the door.") 
                room4()  # Go to room 4 
            else: 
                print("You don't have a golden coin to throw at the dragon!")
                break 
        #if the player chooses to go back, it will print that they returned to the treasure room
        #and then it will take them back to room 2
        elif choice == "3":
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
    print("There is a door to the right and a door to the left.")
    print("1. yes") 
    print("2. no")
 #input for the player to choose whether they want to open the chest or not
    choice = input("Do you want to open the chest? (1/2): ").strip().lower()
    #if they choose yes, it will check if they have the golden coin in their inventory 
    #and if they don't, it will add it to their inventory
    if choice == "1":
        if "golden coin" not in inventory:
            print("You found a golden coin!")
            inventory.append("golden coin")
        else:
            print("The chest is empty. You already took the coin.")
    else:
        print("You decided not to open the chest.")
    #what happens after the player has opened the chest or not 
    
    #if they go through the left door, it will take them to room 1 and make a full circle. whereas if they go through the right door, it will take them to room 3
    print("1. left door") 
    print("2. right door")
    choice = input("Do you want to go through the left door or right door? (1/2): ").strip().lower()
    if choice == "1":
        room1()
    elif choice == "2":
        room3()
    #and if the player chooses an invalid option, it will print that they need to choose a valid option
    else:
        print("Invalid choice. You stay in the room.")


#room 1 code
def room1():
    global lives
    print("\nYou are in a dark room. There is a door infront of you.")
    print("There is a shiny object on the ground.") 
    print("1. yes")
    print("2. no")
    choice = input("Do you want to pick it up? (1/2)").strip().lower() 
    
    if choice == "1":
        if "shiny object" not in inventory:
            inventory.append("shiny object")
            print("You picked up the shiny object.")
        else:
            print("You already picked it up.")
    else:
        print("You left the shiny object on the ground.")
    print("1. yes")
    print("2. no")
    choice = input("Do you want to go through the door? (1/2): ").strip().lower()
    if choice == "1":
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