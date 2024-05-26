


roomList = {'start' : {'description' : "Room description.", 'cardinals' : ['north', 'south', 'east', 'west'], 'directions' : {'north' : 'north hallway', 'south' : 'south hallway', 'east' : 'east hallway', 'west' : 'west hallway'}, 'items' : ['sword', 'bed']},
            'north hallway' : {'description' : 'This is the North Hallway', 'cardinals' : ['south', 'east', 'west'], 'directions' : {'south' : 'start', 'east' : 'northeast tower', 'west' : 'northwest tower'}, 'items' : []}, 
            'south hallway' : {'description' : 'This is the South Hallway', 'cardinals' : ['north', 'east', 'west'], 'directions' : {'north' : 'start', 'east' : 'southeast tower', 'west' : 'southwest tower'}, 'items' : []},
            'east hallway' : {'description' : 'This is the East Hallway', 'cardinals' : ['south', 'north', 'west'], 'directions' : {'south' : 'southeast tower', 'north' : 'northeast tower', 'west' : 'start'}, 'items' : []},
            'west hallway' : {'description' : 'This is the West Hallway', 'cardinals' : ['south', 'east', 'north'], 'directions' : {'south' : 'southwest tower', 'east' : 'start', 'north' : 'northwest tower'}, 'items' : []},
            'northeast tower' : {'description' : 'This is the Northeast tower.', 'cardinals' : ['up', 'south', 'west'], 'directions' : {'up' : 'northeast tower balcony', 'south' : 'east hallway', 'west' : 'north hallway'}, 'items' : []}}

start = {'Description' : "Room description.", 'cardinals' : ['north', 'south', 'east', 'west'], 'directions' : {'north' : 'North Direction', 'south' : 'South direction', 'east' : 'east direction', 'west' : 'West direction'}, 'Items' : ['Item1', 'Item2']}
items = {"sword" : {'description' : 'Item1 description', 'pickupable': 'yes', 'type' : 'weapon'}, 
         'bed' : {'description' : 'Item2 description', 'pickupable': 'no', 'type' : 'bed'}}
# Item format {description, Pickupable, class, uses, equipable, stat modifiers}
## 'northwest tower'
## 'southeast tower'
## 'southwest tower'
currentRoom = 0
currentRoomName = 0
inventory = []
# room_check loads the room 
def room_check(room):
    global currentRoomName
    global currentRoom
    currentRoomName = room
    currentRoom = roomList[room]
    if len(currentRoom['items']) == 0:
        itemList = 'nothing'
    else:
        itemList = ' '.join(currentRoom['items'])
    if len(currentRoom['cardinals']) == 0:
        cardinal = 'nowhere'
    else:
        cardinal = ' '.join(currentRoom['cardinals'])
    print(currentRoom['description'])
    print('You can go ' + cardinal)
    print('You can see ' + itemList + ' on the ground')
# use allows the player to use objects in the room and in their inventory
def use(object, subject):
    print('TODO')
# go takes the player in the specified cardinal direction
def go(direction):
    lastroom = currentRoom
    cardinal = currentRoom['directions']
    try:
        room_check(cardinal[direction])
    except KeyError:
        print('looks like you can\'t go that way')

def look(subject):
    if subject == currentRoomName:
        room_check(currentRoomName)
        return
    try:
        s = items[subject]
    except KeyError:
        print('What are you looking at?')
        return
    print(s['description'])
def pickup(subject):
    item = items[subject]
    if item['pickupable'] == 'no':
        print('You can\'t pick that up')
        return
    roomitems = currentRoom['items']
    i = 0
    while (i >= len(roomitems)) is False:
        if roomitems[i] == subject:
            picked_up = roomitems.pop(i)
            inventory.append(picked_up)
            print('you picked up the ' + subject)
            return
        i = i+1
def drop(subject):
    i = 0
    while (i >= len(inventory)) is False:
        if inventory[i] == subject:
            dropped = inventory.pop(i)
            currentRoom['items'].append(dropped)
            print('you dropped the ' + subject)
            return
# main is the primary loop, instruction returns here after a function has resolved.
def main():
    if currentRoom == 0:
        room_check('start')
    while True == True:
        call = input('What do you do?\n')
        call = call.split(' ')
        if call[0] == 'look' or call[0] == 'Look':
            if len(call) >= 3:
                call2 = []
                call2.append(call[1])
                call2.append(call[2])
                call.pop(1)
                call.pop(1)
                call.append(call2)
            try:
                look(call[1])
            except IndexError:
                print('Lets you look at things.')
        elif call[0] == 'exit' or call[0] == 'Exit':
            return
        elif call[0] == 'use' or call[0] == 'Use':
            try:
                use(call[1], call[2])
            except IndexError:
                try:
                    use(call[1])
                except IndexError:
                    print('Lets you use things, potentially on other things.')
        elif call[0].lower() == 'go':
                try:
                    go(call[1])
                except IndexError:
                    print("Let's you go places")
        elif call[0].lower() == 'pickup':
            try:
                pickup(call[1])
            except IndexError:
                print('let\'s you pick stuff up')
        elif call[0].lower() == 'drop':
            try:
                drop(call[1])
            except IndexError:
                print('Let\'s you drop things.')
        else:
            print('What are you doing?')
        


main()