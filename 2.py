lives = 3  #number of lives the player has 
def lose_life():
    global lives  # Use the global variable 'lives'
    if lives > 0:  # Check if the player has lives left
        lives -= 1  # Decrease the number of lives by 1
        print(f"You lost a life! Lives remaining: {lives}")
    else:
        print("Game Over! No lives left.")   
print("you are in a dark room, you can see a door to the left and a door to the right") 
print("question: which door do you want to go through?")
choice = input("Type 'left' for the left door or 'right' for the right door: ").strip().lower() 
if choice == "left":
    print("You chose the left door. You find a treasure chest!")
    print("Congratulations! You win the game!")
