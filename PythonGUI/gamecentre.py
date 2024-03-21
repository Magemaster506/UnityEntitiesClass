program_name = "name"
user_prompt = "enter input"

print(program_name)
print(user_prompt)

option1 = "1.snake"
option2 = "2.chess"
option3 = "3.car"
option4 = "4.quit"

def displayList(input):
    if input == "4":
        print("Quit")
    else:  
        print(option1)
        print(option2)
        print(option3)

choice = int(input(""))

if choice > 4 or choice < 1:
    print("That choice is not valid..")
    choice = int(input(""))
else:
    if choice == 1:
        print("playing 1")