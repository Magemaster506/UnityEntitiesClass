# Select a random element from a list
import random


# List of animals stored in a list
animals = ["Dog", "Cat", "Cow", "Chicken"]


# This starts the loop for selecting and printing the random animals
# The loop will execute 10 times
for i in range(1, 11):
   # Random selection of elements from the list
   selected_animal1 = random.choice(animals)
   selected_animal2 = random.choice(animals)


   # Display results
   print("Animal 1: ", selected_animal1)
   print("Animal 2: ", selected_animal2)
   print()


   # Decision Structure to check for compatibility
   if selected_animal1 == "Dog" and selected_animal2 == "Cat":
       print ("Dog chases cat!")
   elif selected_animal1 == "Cat" and selected_animal2 == "Dog":
           print("Cat scratches dog!")
   elif selected_animal1 == "Chicken" and selected_animal2 == "Cow":
       print("Chicken pecks cow!")
   elif selected_animal1 == "Cow" and selected_animal2 == "Chicken":
       print("Cow moos at chicken!")
   else:
       print(selected_animal1, "and", selected_animal2, "get along fine!")


   print()