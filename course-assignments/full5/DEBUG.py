from sys import argv

for arg in argv:
    if arg == "DEBUG":
        print("Starting in DEBUG mode:")
        DEBUG = True
    else:
        DEBUG = False

def dprint(user_input):
    # AUTHOR: Lars Hedlund
    # FUNCTION: Prints debugging values to help with logic errors
    # INPUT: string
    # RETURN: none
    if DEBUG == True:
        print("<<<", user_input, ">>>")
