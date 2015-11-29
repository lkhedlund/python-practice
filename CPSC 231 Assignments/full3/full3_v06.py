"""
HEADER: Command Line Parser by Lars Hedlund
Features: (1) Input from file (2) -T evalutes correctly (3) Error reporting works
(4) System arguments (need testing) (3) +t evaulates correctly
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
        #error_report("TF", arg)
        print("ERROR!")
    elif (len(arg) == 2): # checks for a number after T
        return RATIO_DEFAULT
    elif 2 <= int(arg[2]) <= 8: # checks that integer is within defined range
        ratio = int(arg[2])
        return ratio
    elif (int(arg[2]) > 8) or (int(arg[2]) < 2): # check if out of range
        #return error_report("TR", arg)
        print("ERROR!")
    else:
        print("ERROR!")
        #return error_report("FATAL", arg)

def positive_t(line, ratio): # bug fixed
    """
    (F)unction: positive t replaces prefix sequences of spaces of length T
    with a single tab.
    (I)nput: string, integer
    (R)eturn: string
    """
    lead_len = len(line) - len(line.lstrip())
    lead_line = line[0:lead_len]
    tab_length = chr(32) * ratio
    tabbed_line = str()
    new_line = str()
    trailing_sp = str()

    # checks to see if the line is long enough to replace
    if chr(9) in lead_line: # if the line is long enough, look for a tab to preserve trailing spaces
        trailing_sp = lead_line[len(lead_line.rstrip(chr(32))):lead_len] # preserved spaces
        lead_line = lead_line.replace(tab_length, chr(9)) # first replace the spaces with tabs
        for ch in lead_line: #then, to remove internal spaces, create only tabs
            if ch == chr(9):
                tabbed_line += ch
        if trailing_sp >= tab_length: # if the trailing spaces and ratio are the same, they would have already been converted
            line = tabbed_line + line.lstrip()
            return line
        else:
            line = tabbed_line + trailing_sp + line.lstrip() # if they weren't converted to tabs, add back.
            return line
    else: # if there is no tab, just convert the line and return it
        if lead_len < len(tab_length):
            return line
        else:
            new_line = lead_line.replace(tab_length, chr(9))
            line = new_line + line.lstrip()
            return line

def negative_t(line, ratio):
    """
    (F)unction: negative t replaces prefix tabs with sequences of T spaces.
    (I)nput: string, integer
    (R)eturn: string
    """
    lead_len = len(line) - len(line.lstrip())
    lead_line = line[0:lead_len]
    tab_length = chr(32) * ratio
    tabbed_line = str()
    new_line = str()
    trailing_sp = str()

    if chr(9) in lead_line:
        trailing_sp = lead_line[len(lead_line.rstrip(chr(32))):lead_len]

    for ch in lead_line:
        if ch == chr(9):
            tabbed_line += ch
    new_line = tabbed_line.replace(chr(9), tab_length)
    line = new_line + trailing_sp + line.lstrip()

    if line != EOF:
        return line
    else:
        return EOF

def positive_v(line):
    """
        replace_space = line.replace(chr(32), SPACE_CHAR)
        replace_tabs = replace_space.replace(chr(9), TAB_CHAR) + chr(9)
        print(replace_tabs)
    """
    new_line = ""
    if line != EOF:
        for ch in line:
            if ch == chr(32):
                new_line += ch.replace(chr(32), SPACE_CHAR)
            elif ch == chr(9):
                new_line += ch.replace(chr(9), TAB_CHAR)
            else:
                new_line += ch
        line = new_line.rstrip() + NEWLINE_CHAR
        return line
    else:
        return line

def negative_v():
    pass

def help_text():
    print("HELP!")

def error(error_code, user_input):
    """
    TF print("Tab sizes greater than 8 or less than 2 are not allowed: %s" % error)
    TR print("The -T qualifier must be immediately followed by an integer: %s" % error)
    FATAL print
    UA Unrecognized argument
    help print("Help is not the only argument.")
    return "Error %s: %r" % (error_code, user_input)
    """
    pass

def main(): # bug in how it treats "other arguments"
    firstArg = False
    output = ""
    error_report = "None"
    """
    print(sys.argv)
    for arg in sys.argv:
        print(arg)
        if (arg in "-T"):
            ratio = upper_t(arg)
        else:
            ratio = RATIO_DEFAULT
    print("Ratio is", ratio)
    """
    ratio = RATIO_DEFAULT

    if ("-t" in sys.argv) and ("+t" in sys.argv):
        #error_report += error("t", arg)
        print(True)
    elif ("-v" in sys.argv) and ("+v" in sys.argv):
        #error_report += error("v", arg)
        pass
    else:
        line = getInput()
        while (line != EOF):
            line = getInput()
            for arg in sys.argv:
                if firstArg:
                    firstArg = False
                elif (firstArg == False) and len(sys.argv) == 1:
                    line = line
                elif (arg == "-t"):
                    line = negative_t(line, ratio)
                elif (arg == "+t"):
                    line = positive_t(line, ratio)
                elif (arg == "-v"):
                    line = negative_v()
                elif (arg == "+v"):
                    line = positive_v(line)
                """
                elif (arg[0:1] in "-hH") and (len(sys.argv) != 2):
                    #error_report += error("help", arg)
                    pass
                elif (arg[0:1] in "-hH") and (len(sys.argv) == 2):
                    print(help_text())
                    exit(0)
                elif (len(sys.argv) <= 1):
                    #copy input to output
                    print(line)
                elif (("<" or ">") in arg):
                    pass
                """
            print("%r" % line)

main()
