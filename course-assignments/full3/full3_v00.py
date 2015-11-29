"""
Testing version
"""
import sys

# Global Constants
EEOF = chr(4)           # A standard End-Of-File character (ascii value 4)

TAB_CHAR = chr(187)     # A ">>" character (as a single character) in the extended ascii set
                        #   Used to make a tab character visible.
SPACE_CHAR = chr(183)   # A raised dot character in the extended ascii set
                        #   Used to make a space character visible
NEWLINE_CHAR = chr(182) # A backwards P character in the extended ascii set
                        #   Used to make a newline character visible

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
    print("Success!")

def negative_t():
    print("Success!")

def upper_t(arg):
    sptab_ratio = None # space to tab ratio
    if (arg == "-T"):
        sptab_ratio = 4
        print(arg, sptab_ratio)
    elif 2 <= int(arg[2]) <= 8:
        sptab_ratio = int(arg[2])
        print(arg, sptab_ratio)
    elif (int(arg[2]) > 8) or (int(arg[2]) < 2):
        print("Tab sizes greater than 8 or less than 2 are not allowed: %s" % arg)
    else:
        print("The -T qualifier must be immediately followed by an integer: %s" % arg)

def positive_v():
    print("Success!")

def negative_v():
    print("Success!")

def help_text(t, v, T, h):
    if t == True:
        print("Qualifiers +t and -t cannot both be used together.")


def main():
    firstArg = True
    for arg in sys.argv:
        print(arg)
        if firstArg:
            firstArg = False
        elif (arg == "+t"):
            if "-t" in sys.argv:
                help_text(True, pass, pass, pass)
                break
            else:
                positive_t()
        elif (arg == "-t"):
            if "+t" in sys.argv:
                help_text(True, pass, pass, pass)
                break
            else:
                negative_t()
        elif (arg[0:2] == "-T"):
            upper_t(arg)
        else:
            print("Something went wrong")





main()
