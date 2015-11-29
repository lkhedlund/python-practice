"""
HEADER: Command Line Parser by Lars Hedlund
Features: (1) Input from file (2) -T evalutes correctly (3) Error reporting works
(4) Main function works through system arguments
Version: 0.2
"""
import sys

# Global Constants
EOF = chr(4)           # A standard End-Of-File character (ascii value 4)

TAB_CHAR = chr(187)     # A ">>" character (as a single character) in the extended ascii set
                        #   Used to make a tab character visible.
SPACE_CHAR = chr(183)   # A raised dot character in the extended ascii set
                        #   Used to make a space character visible
NEWLINE_CHAR = chr(182) # A backwards P character in the extended ascii set
                        #   Used to make a newline character visible
RATIO_DEFAULT = 4       # The default number for the space-to-tab ratio

# Main functions
def getInput():
    """This function works exactly like input() (with no arguments), except that,
    instead of throwing an exception when it encounters EOF (End-Of-File),
    it will return an EOF character (chr(4)).

    Returns: a line of input or EOF if EOFError occurs during input.
    """
    try:
        ret = input()
    except EOFError:
        ret = EOF
    return ret

def positive_t():
    """
    (F)unction:
    """
    while line != EOF:
        line = getInput()
        print("Original:")
        print(line)
        rem_tab = line.lstrip(chr(9))
        print("Tabs removed:")
        print(rem_tab)
        print("Spaces replaced:")
        sp_replace = line.replace(chr(32), chr(183))
        print(sp_replace)
        print("----------------")

def negative_t():
    pass

def upper_t(arg):
    """
    (F)unction: Takes a user's provided argument for T and checks for correct
    values. If correct, returns the space-to-tab ratio. If incorrect, returns
    an error.
    (I)nput: string
    (R)eturn: string, integer
    """
    sptab_ratio = None # space to tab ratio
    if ("." in arg): # checks for a floating point number
        error_report("TF", arg)
    elif (len(arg) == 2): # checks for a number after T
        return RATIO_DEFAULT
    elif 2 <= int(arg[2]) <= 8: # checks that integer is within defined range
        sptab_ratio = int(arg[2])
        return sptab_ratio
    elif (int(arg[2]) > 8) or (int(arg[2]) < 2): # check if out of range
        return error_report("TR", arg)
    else:
        return error_report("FATAL", arg)


def positive_v():
    pass

def negative_v():
    pass

def help_text():
    pass

def error_report(error_code, user_input):
    """
    TF print("Tab sizes greater than 8 or less than 2 are not allowed: %s" % error)
    TR print("The -T qualifier must be immediately followed by an integer: %s" % error)
    FATAL print
    UA Unrecognized argument
    """
    print("Error %s: %r" % (error_code, user_input))

def main():
    sptab_ratio = 0
    firstArg = True
    for arg in sys.argv:
        if firstArg:
            firstArg = False
        elif (arg == "-t"):
            negative_t()
        elif (arg == "+t"):
            positive_t()
        elif ("-T" in arg):
            print(upper_t(arg))
        elif (arg == "-v"):
            negative_v()
        elif (arg == "+v"):
            positive_v()
        elif (arg[0:1] in "-hH"):
            help_text()
        elif (len(sys.argv) < 1):
            #copy input to output
            pass
        else:
            error_report("UA", arg)

main()
