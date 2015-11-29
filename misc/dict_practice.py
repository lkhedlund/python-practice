rooms = {
    'the Study': 'the knife',
    'the Kitchen': 'the crowbar',
    'the Lounge': 'the revolver',
    'the Ball Room': 'the lead pipe'
}

murderers = {
    'the knife': 'Mr. Green',
    'the crowbar': 'Mrs. Scarlet',
    'the revolver': 'Mrs. White',
    'the lead pipe': 'Professor Plum'
}

print "Welcome to Clue!"
print "Where do you think the murder was committed?"

def room_guess():
    flag = True
    while flag == True:
        user_input = raw_input("> ")
        if user_input in rooms:
            print "%s has %s" % (user_input, rooms[user_input])
            flag = False
            murder_guess(user_input, rooms[user_input])
        elif user_input == "help":
            for key, value in rooms.items(): # pulls both key and value but only returns one. "for key in rooms" returns the whole dict.
                print key
        else:
            print "That isn't a room. Try typing 'help' for more info."

def murder_guess(room, weapon):
    print "So far, we have '%s' and '%s'" % (room, weapon)
    print "Who do you think committed the murder?"
    flag = True
    while flag == True:
        user_input = raw_input("> ")
        if user_input == "help":
            for key, value in murderers.items():
                print value
        elif user_input == murderers[weapon]:
            print "You did it! You solved the murder."
            print "It was %s, in %s, with %s." % (user_input, room, weapon)
            flag = False
        elif user_input != murderers[weapon]:
            print "You did not solve the murder. Please try again."
        else:
            print "I do not understand. Try typing 'help'"


room_guess()
