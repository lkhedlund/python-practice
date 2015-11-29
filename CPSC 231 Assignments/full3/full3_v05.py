"""
HEADER: Command Line Parser by Lars Hedlund
Features: (1) Input from file (2) -T evalutes correctly (3) Error reporting works
(4) System arguments (need testing)
Version: 0.5
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

def positive_t(line, ratio):
    """
    (F)unction: positive t
    (I)nput: string, integer
    (R)eturn: string
    """
    lead_len = len(line) - len(line.lstrip()) # length of leading space
    lead_line = line[0:lead_len] # leading space
    tab_length = chr(32) * ratio # space to tab ratio
    trailing_sp = lead_line[len(lead_line.rstrip(chr(32))):lead_len] # spaces removed after the last tab
    new_line = str()

    line = lead_line.replace(tab_length, chr(9))
    for ch in line:
        if ch == chr(9):
            new_line += ch
    new_line += trailing_sp + line.lstrip() # add new tab stops, trailing spaces, and remaining text
    return new_line

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
    ratio = None # space to tab ratio
    if ("." in arg): # checks for a floating point number
        error_report("TF", arg)
    elif (len(arg) == 2): # checks for a number after T
        return RATIO_DEFAULT
    elif 2 <= int(arg[2]) <= 8: # checks that integer is within defined range
        ratio = int(arg[2])
        return ratio
    elif (int(arg[2]) > 8) or (int(arg[2]) < 2): # check if out of range
        return error_report("TR", arg)
    else:
        return error_report("FATAL", arg)


def positive_v():
    line = getInput()
    while (line != EOF):
        line = getInput()
        replace_space = line.replace(chr(32), SPACE_CHAR)
        replace_tabs = replace_space.replace(chr(9), TAB_CHAR) + chr(9)
        print(replace_tabs)

def negative_v():
    pass

def help_text():
    pass

def error(error_code, user_input):
    """
    TF print("Tab sizes greater than 8 or less than 2 are not allowed: %s" % error)
    TR print("The -T qualifier must be immediately followed by an integer: %s" % error)
    FATAL print
    UA Unrecognized argument
    help print("Help is not the only argument.")
    """
    print("Error %s: %r" % (error_code, user_input))

def main():
    ratio = RATIO_DEFAULT
    t_qualifier = False
    v_qualifier = False
    output = ""
    error_report = None

    line = getInput()
    while (line != EOF):
        line = getInput()
        for arg in sys.argv:
            if firstArg:
                firstArg = False
            elif ("-T" in arg):
                ratio = upper_t(arg)
            elif (arg == "-t") or (arg == "+t") and (t_qualifier == True):
                error_report += error(t, arg)
            elif (arg == "-t"):
                t_qualifier = True
                output += negative_t(line, ratio)
            elif (arg == "+t"):
                t_qualifier = True
                output += positive_t(line, ratio)
            elif (arg == "-v") or (arg == "-v") and (v_qualifier == True):
                error_report += error(v, arg)
            elif (arg == "-v"):
                v_qualifier = True
                output += negative_v()
            elif (arg == "+v"):
                v_qualifier = True
                output += positive_v()
            elif (arg[0:1] in "-hH") and (len(sys.argv) != 2):
                error_report += error("help", arg)
            elif (arg[0:1] in "-hH") and (len(sys.argv) == 2):
                print help_text()
                exit(0)
            elif (len(sys.argv) <= 1):
                #copy input to output
                print line
            else:
                error_report += error("UA", arg)

    if error_report != None:
        print output
    else:
        print error_report
        exit(0)

main()
