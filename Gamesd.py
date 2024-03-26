in_menu = True
command = ""
itemnum = -1

############ Def the start message ##################
def clear_screen():   
    print("-------------------------------------------------------------------")
    print("")
    for x in range(30):
        print("")

def intro():    
    print("-------------------------------------------------------------------")
    print("")
    print("Welcome to Sam Lucas's Text Based Adventure Game!")
    print("")
    print("Below are some things you can ask and where you can start the game")
    print("")
    print("Instructions = i, Play Game = Enter, Story = s")
    print("")
    
############### Menu Choices ########################
clear_screen()

while in_menu == True:
    
    intro()
    menu_choice = input("Prompt: ")
    
    if menu_choice == "i":
        print("-------------------------------------------------------------------")
        print("")
        print("You interact with the game using short commands such as single")
        print("characters 'i', 'g' or short commands 'stay', 'leave'")
        print("All options will be on screen to help let you know what to do")
        print("")
        print("-------------------------------------------------------------------")
        print("")
        print("To go back to the menu, type 'm' ")
        print("")
        input("Prompt :")
    elif menu_choice == "s":
        print("-------------------------------------------------------------------")
        print("")
        print("You woke up in a dark place, you feel scared but you feel like you")
        print("know this place, like you've been here before. After looking around")
        print("you see that you're stuck inside of your school? How could this be?")
        print("no one is around, well you though nobody was around untill you ")
        print("hear a gurgling noise outside of the locked classroom you're inside")
        print("")
        print("-------------------------------------------------------------------")
        print("")
        print("To go back to the menu, type 'm' ")
        print("")
        input("Prompt :")
    else:
        in_menu == False
        break

################ Game Setup  ############################

rooms = {

        'English Room' : { 'name' : 'English Room', 'Item':'Crowbar', 'Enemy':'Zombie', 'found':'N', 'n':'Hallway', 'defeated':'N',
                           'story':'You wake up, nauseous. You are confused as you look around and \nsee that you are inside of an english room, but its dark it is \nnight time but something does not seem right... \nsomething is banging outside \n \nOptions: Search = search, Go Through the Door = n'},
        'Hallway' : {'name': 'Hallway', 'back':'N', 'Item': 'Wooden Plank', 'Enemy': 'Infectious Dog', 'found':'N', 's': 'English Room', 'w': 'Quad', 'defeated': 'N',
                     'story':'You break open the door with the Crowbar and find the\nabsolutely horrifying state the school was in, dirt, moss and crubling walls. \njust as you start walking down the hallway, a infected looking dog \njumps out, the dog was agressive and yeering. \n\nWhat do you do? Search = search, Go west down hall = w, Go back inside = s \nType item to use against dog'},
        'Quad' : {'name': 'Quad', 'Item': 'Mallet', 'Enemy': 'Hole', 'found':'N', 'w': 'Hidden', 'defeated': 'N', 's': 'Hallway' ,
                  'story':'After beating the infectious dog with a Crowbar, \nyou head through into the Quad through the west hall, you are \nsurrounded by zombies from your left and right and behind a group of \n6 zombies follow after you into the quad. There is a giant sink hole \nin the middle of the quad you can not find a way around it \n\nWhat do you do? Search = search, Run = run, Go back into Hall = s \nOr you can use an item'},
        'Hidden' : {'name': 'Hidden', 'Item': 'Nothing', 'Enemy': 'The Unknown', 'defeated': 'N', 'story':''},
    }

current_location = rooms['English Room']
commands = [['n','s','e','w'],['search']]
inventory = []
notitem = ""


def game_window():
    clear_screen()
    print("####################################################################")
    print("")
    print(f" Location = {current_location['name']}")
    print("")
    print(f" Inventory = {inventory}")
    print("")
    if current_location['defeated'] == "N":
        print(f"Story : {current_location['story']}\n")
    print("####################################################################")
    print("")
    print(notitem)
    
    if current_location['found'] == "Y":
        print(f"#!#!#!#!#You found a {inventory[itemnum]}#!#!#!#!#")
    

################# Main Loop ##############################

while True:
    current_location['found'] == "N"
    game_window()
    notitem = ""
    command = input("\nWhat would you like to do? ")

## if input is direction ##
    
    if command.strip().lower() in commands[0]:
        if command in current_location:
            if current_location['name'] == 'English Room':
                if current_location['found'] == "Y":
                    current_location = rooms[current_location[command]]
                else:
                    notitem = "Ugh, can't open the door..."      
            elif current_location['name'] == 'Hallway':
                if current_location['defeated'] == "Y":
                    current_location = rooms[current_location[command]]
                elif command.strip().lower() == "s":
                    clear_screen()
                    clear_screen()
                    print("You Died")
                    input()
                    break
                elif command.strip().lower() == "w":
                    if current_location['back'] != 'Y':
                        clear_screen()
                        clear_screen()
                        print("You Died")
                        input()
                    else:
                        current_location = rooms[current_location[command]]
                        rooms['Hallway']['defeated'] = "Y"
            elif current_location['name'] == 'Quad':
                if (rooms['Hallway']['defeated']) == "Y":
                    rooms['Hallway']['defeated'] = "N"
                    rooms['Hallway']['story'] = "You run back into the hallway and the infectious dog seems \nto be dying, it's bleeding out and crawled into a ball \nWhat do you do? Search = search, Go west down hall = w, Go back inside = s \nType item to use against dog"
                    rooms['Hallway']['back'] = "Y"
                    current_location = rooms[current_location['s']]
                    

## if input is search ##                    

    if command.strip().lower() in commands[1]:
        if command.lower().strip() == "search" and current_location['Item'] !='Nothing':
            inventory.append(""+current_location['Item'])
            current_location['Item'] = "Nothing"
            current_location['found'] = "Y"
            itemnum += 1

## using item ##

    if command.strip() in inventory:
        if command.strip() == "Crowbar":
            if current_location['name'] == 'Hallway':
                current_location['defeated'] = "Y"
                current_location = rooms[current_location['w']]
        


    if command.strip().lower() == "run":
        if current_location['name'] == 'Quad': 
            clear_screen()
            clear_screen()
            print("You Died")
            input()
    
                             
        
















