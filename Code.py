print("\nWelcome to Animals Name Guessing Game:)\nAvailable names are as follows: \n")

import random
Animals = ["Cow", "Cat", "Dog", "Monkey","Donkey"]
print(Animals)
words = random.choice(Animals)
print(words) # We can remove this to hide from the user

for i in range(3):
    Animal = input("Enter your guess from these names: ").strip()  

    if Animal.lower() ==words.lower():
        print("Heyyy You Won:) , You are a Genius!")
        break;
    else:
        print("Incorrect guess. Try again! :)") 
print("Game Over!!!")        
   
