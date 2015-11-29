"""
HEADER: Command Line Parser by Lars Hedlund
Features: (1) Input from file (2) -T evalutes correctly (3) Error reporting works
(4) System arguments (need testing) (5) +t evaulates correctly (6) -t evaluates
correctly (7) +v evaluates correctly
Bugs: None!
Version: 0.7
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
    ratio = 4 # space to tab ratio
    if ("." in arg): # checks for a floating point number
        return ratio, error("TF", arg) + '\n'
    elif (len(arg) == 2): # checks for a number after T
        return RATIO_DEFAULT, "None"
    elif 2 <= int(arg[2]) <= 8: # checks that integer is within defined range
        ratio = int(arg[2])
        return ratio, "None"
    elif (int(arg[2]) > 8) or (int(arg[2]) < 2): # check if out of range
        return ratio, error("TI", arg)  + '\n'
    else:
        return ratio, error("Runtime", None)  + '\n'

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
    count = 0
    lead_len = len(line) - len(line.lstrip())
    lead_line = line[0:lead_len]
    tab_length = chr(32) * ratio
    new_line = str()
    trailing_sp = str()

    # check to see if there is a tab
    if chr(9) not in lead_line:
        # if there isn't a tab, return the line
        return line
    else:
        for ch in lead_line:
            if ch == chr(32):
                count += 1
            elif (ch == chr(9)) and (count < len(tab_length)):
                new_line += tab_length
                count = 0
            elif (ch == chr(9)) and (count >= len(tab_length)):
                new_line += (chr(32) * count) + tab_length
                count = 0
            else:
                return error("Runtime", None)
        trailing_sp = chr(32) * count
        line = new_line + trailing_sp + line.lstrip()
        return line

def positive_v(line):
    new_line = ""
    if line != EOF:
        for ch in line:
            if ch == chr(32):
                new_line += ch.replace(chr(32), SPACE_CHAR)
            elif ch == chr(9):
                new_line += ch.replace(chr(9), TAB_CHAR) + chr(9)
            else:
                new_line += ch
        line = new_line.rstrip() + NEWLINE_CHAR
        return line
    else:
        return line

def negative_v(line):
    new_line = ""
    if line != EOF:
        for ch in line:
            if ch == SPACE_CHAR:
                new_line += ch.replace(SPACE_CHAR, chr(32))
            elif ch == TAB_CHAR:
                new_line += ch.replace(TAB_CHAR, chr(9))
            elif ch == NEWLINE_CHAR:
                new_line += ch.replace(NEWLINE_CHAR, '\n')
            else:
                new_line += ch
        return line
    else:
        return line

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
    if error_code == "TF":
        return "The -T qualifier must be immediately followed by an integer: %s" % user_input
    elif error_code == "TI":
        return "Tab sizes greater than 8 or less than 2 are not allowed: %s" % user_input
    elif error_code == "BT":
        return "Qualifiers +t and -t cannot both be used together."
    elif error_code == "BV":
        return "Qualifiers +v and -v cannot both be used together."
    elif error_code == "UA":
        return "Unrecognized Argument: %s" % user_input
    elif error_code == "HP":
        return "-help was not the only argument passed."
    else:
        return "Major Runtime Exception Occurred. Program will now stop."
        exit(0)

def main(): # bug in how it treats "other arguments"
    output = ""
    error_report = ""

    print(sys.argv)
    for arg in sys.argv:
        if ("-T" in arg):
            ratio, error_report = upper_t(arg)
        else:
            ratio = RATIO_DEFAULT
    print("Ratio is", ratio)

    if ("-t" in sys.argv) and ("+t" in sys.argv):
        error_report += error("BT", arg) + '\n'
    if ("-v" in sys.argv) and ("+v" in sys.argv):
        error_report += error("BV", arg) + '\n'
    line = getInput()
    while (line != EOF):
        line = getInput()
        for arg in sys.argv:
            if arg in sys.argv[0]:
                pass

            elif (arg == "-t"):
                line = negative_t(line, ratio)
            elif (arg == "+t"):
                line = positive_t(line, ratio)
            elif (arg == "-v"):
                line = negative_v(line)
            elif (arg == "+v"):
                line = positive_v(line)
            elif (arg[0:1] in "-hH") and (len(sys.argv) == 1):
                print(help_text())
                exit(0)
            elif (len(sys.argv) <= 1):
                #copy input to output
                print(line)
            else:
                error_report += error("UA", arg) + '\n'
        if error_report != "":
            print("The following errors have occurred:")
            print(error_report)
            print("""
Acceptable Commands: [+t] [-t] [-T<integer>] [+v] [-v] [-help]
+t          -replaces prefix sequences of spaces of length T with a single tab
-t          -replaces prefix tabs with sequences of T spaces
-T<integer> -the <integer> defines the space-to-tab ratio, T (default=4)
+v          -changes all spaces, tabs, and newlines to printable characters
-v          -reverses the changes made by +v
-help       -prints out help text if -help is the only argument

+t and -t cannot be passed as arguments together
+v and -v cannot be passed as arguments together
            """)
            exit(0)
        else:
            print("%r" % line)

main()
