#ZION JOHNSON
rooms = {
    'Your Room': {'Exit': 'Exit', 'East': 'Hallway',},
    'Hallway': {'Exit': 'Exit', 'North': 'Entryway', 'East': 'Little Brothers Room', 'South': 'Living Room', 'West': 'Your Room', 'item': 'Mr. Mittens'},
    'Living Room': {'Exit': 'Exit', 'North': 'Hallway', 'East': 'Garage', 'South': 'The Kitchen', 'West': 'Patio', 'item': 'Battery'},
    'Entryway': {'Exit': 'Exit', 'South': 'Hallway', 'item': 'Pair of Slippers'},
    'Little Brothers Room': {'Exit': 'Exit', 'West': 'Hallway', 'item': 'Flashlight'},
    'Patio': {'Exit': 'Exit', 'East': 'Living Room', 'item': 'Stick'},
    'Garage': {'Exit': 'Exit', 'West': 'Living Room', 'item': 'String'},
    'The Kitchen': {'Exit': 'Exit', 'North': 'Living Room', 'item': 'Dad'},
    'Exit': 'Exit'
} # This is a dictionary for us to draw from in our functions
def itemcheck(player_input, currentroom): #define function call itemcheck
        print('There seems to be a', rooms[currentroom]['item'], 'present. Would you like to take it?')
        input1 = input('Enter: y/n\n') # checks for input and prints a message
        if input1 == 'y': #if the play's input is 'y'
            print('Added', rooms[currentroom]['item'], 'to inventory.') #prints a message stating that the item in that nested dictionary's room was added to the inventory
            inventory.append(rooms[currentroom]['item']) #This adds the said item onto the back of the list called inventory
            rooms[currentroom].pop('item') #this removes the item from the dictionary so that it can't be collected again
        if input1 == 'n': #if players inputs 'n'
            print('Ignoring Item') #prints 'ignoring item' and then returns to the while loop
def movingfunc(player_input, currentroom): # defines function called movingfunc
    if player_input == 'item': #if player inputs item
        try: #we try the stated conditions, tutor helped me to understand the try and except statements. I decided to use them here since they worked the best
            itemcheck(player_input, currentroom) #itemcheck is a function defined above
            return currentroom #we then return the value of currentroom
        except: #if we were unable to succeed with the values above we do this:
            print('There is no item.') # prints that there is no item
            return currentroom #returns value of currentroom
    elif player_input in rooms[currentroom]: # if player_input equals anything but 'item' it will check if it is a valid direction and then will set currentroom equal to the value inputed by player.
        return rooms[currentroom][player_input]

    else:
        print("Currently not a valid command.") #if neither of the above conditions are met then it just prints that whatever the player entered was not a valid command.
        return currentroom
def bosscheck(): #boss check function
    inventorycount = len(inventory) #assigns the variable inventorycount to the amount of strings in the list inventory.
    if inventorycount == 6: #if the amount of strings is less than 6 it will perform these:
        print('You enter The Kitchen carefully. \nZOINKS! Its your dad!\nYou use your items to blind your father, hiding your identity! You can blame this on your brother!')
        print('CONGRATS! YOU WIN!')
        exit()
    elif inventorycount < 6: #if inventorycount is less than 6 (the required amount) then it will output these:
        print('You got grounded!')
        print('Oops! You came into The Kitchen unprepared... Game Over.')
        exit()
inventory = [] #sets up a list called inventory for use in the functions
print('You awake in the middle of night to a loud crash from the kitchen.', '\nPossible commands include: "North", "East", "South", "West", "Exit" and "item"', '\n---------------') #Opening Text
currentroom = rooms['Hallway']['West'] #Sets the currentroom up as 'your room' which is the planned starting room.
player_input = ''


while currentroom != rooms['Exit']: # As long as the player is not in the exit room it will run this code
    print('You are currently in:', currentroom, '\nInventory:', inventory, '\n---------------', '\nWhat would you like to do?')
    player_input = input() #Checks for player input
    currentroom = movingfunc(player_input, currentroom) #prints message, checks for input, then runs function which will read input
    if currentroom == 'The Kitchen': #after running the movingfunction it will perform this if statement. Checks if the player is in the kitchen if they are then it will call the bosscheck function.
        bosscheck()
