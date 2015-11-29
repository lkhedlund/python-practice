"""
HEADER: Indentation and Space Reader by Lars Hedlund
Features: (1) Input from file (2) -T evalutes correctly (3) Error reporting works
(4) System arguments evaluate correctly (5) +t evaulates correctly (6) -t evaluates
correctly (7) +v evaluates correctly (8) -v evaluates correctly (9) help document
displays as expected
Bugs: None!
Version: 0.9
"""
import sys

# Global Constants
EOF = chr(4)            # A standard End-Of-File character

TAB_CHAR = chr(187)     # A ">>" character in the extended ascii set
                        #   Used to make a tab character visible.
SPACE_CHAR = chr(183)   # A raised dot character in the extended ascii set
                        #   Used to make a space character visible
NEWLINE_CHAR = chr(182) # A backwards P character in the extended ascii set
                        #   Used to make a newline character visible
RATIO_DEFAULT = 4       # The default space-to-tab ratio

# Main functions
def getInput():
    """
    (F)unction: If this input encounters an EOF it returns the EOF constant
    rather than an error.
    (I)nput: None
    (R)eturn: string or EOF
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
        return RATIO_DEFAULT, ""
    elif 2 <= int(arg[2]) <= 8: # checks that integer is within defined range
        ratio = int(arg[2])
        return ratio, ""
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
        if lead_len < len(tab_length): # if the leading space isn't long enough to convert, return it
            return line
        else:
            new_line = lead_line.replace(tab_length, chr(9)) # if the leading space is long enough, apply changes
            line = new_line + line.lstrip()
            return line

def negative_t(line, ratio):
    """
    (F)unction: negative t replaces prefix tabs with sequences of T spaces.
    (I)nput: string, integer
    (R)eturn: string
    """
    count = 0 # initialize count
    lead_len = len(line) - len(line.lstrip()) # length of leading space
    lead_line = line[0:lead_len] # splice of leading space
    tab_length = chr(32) * ratio # length of tabs
    new_line = str() # initialize new line
    trailing_sp = str() # initialize trailing space

    # check to see if there is a tab
    if chr(9) not in lead_line:
        # if there isn't a tab, return the line
        return line
    else:
        # if there is a tab, loop through the line
        for ch in lead_line:
            if ch == chr(32): # if the character is a space, update count
                count += 1
            # if the character is a tab and the count is less than the length of a single tab
            elif (ch == chr(9)) and (count < len(tab_length)):
                # incorporate the spaces into the tab
                new_line += tab_length
                # reset count
                count = 0
            elif (ch == chr(9)) and (count >= len(tab_length)): # if the character is a tab and the count is greater than the length of the tab
                new_line += (chr(32) * count) + tab_length # add the spaces and the tab together.
                count = 0 # reset the count
            else:
                return error("Runtime", None)
        trailing_sp = chr(32) * count # if there are any remaining spaces after the last tab (i.e. count != 0), add them.
        line = new_line + trailing_sp + line.lstrip() # create the new line
        return line

def positive_v(line):
    """
    (F)unction:
    (I)nput:
    (R)eturn:
    """
    new_line = ""
    if line != EOF:# check to see if the line is at the end of the file
        for ch in line: # loop through characters
            if ch == chr(32):
                new_line += SPACE_CHAR # replace spaces with a raised dot
            elif ch == chr(9):
                new_line += TAB_CHAR + chr(9) # replace tabs with '>>' and a tab to preserve formatting
            else:
                new_line += ch # add any additional characters
        line = new_line.rstrip() + NEWLINE_CHAR # replaces the end of the line with the paragraph cahracter and adds \n to preserve format
        return line
    else:
        return line

def negative_v(line):
    """
    (F)unction:
    (I)nput:
    (R)eturn:
    """
    new_line = ""
    if line != EOF: #check to see if the line is at the end of the file
        for ch in line:
            if ch == SPACE_CHAR: # replaces the raised dot with spaces
                new_line += chr(32)
            elif ch == TAB_CHAR: # does not add a tab to the new line since a tab was added in +v
                pass
            elif ch == NEWLINE_CHAR: # does not add a \n since \n was added in +v
                pass
            else:
                new_line += ch # adds all other characters
        return new_line
    else:
        return line

def help_text():
    """
    (F)unction:
    (I)nput:
    (R)eturn:
    """
    print("""
==HELP DOCUMENT==
Indentation and Space Reader

==INSTRUCTIONS==
This program takes an argument using the command line and applies the corresponding
changes to the input document. The commands and changes are as follows:
------------------------------------------------------------------------------
COMMAND     CHANGE
------------------------------------------------------------------------------
+t          -replaces prefix sequences of spaces of length T with a single tab
-t          -replaces prefix tabs with sequences of T spaces
-T<integer> -the <integer> defines the space-to-tab ratio, T (default=4)
+v          -changes all spaces, tabs, and newlines to printable characters
-v          -reverses the changes made by +v
-help       -prints out help text if -help is the only argument
------------------------------------------------------------------------------
Please note that the following arguments cannot be used together:
+t and -t cannot be passed as arguments together
+v and -v cannot be passed as arguments together

==EXAMPLE==
A typical input using Terminal or Powershell should look like the following:
------------------------------------------------------------------------------
PYTHON PROGRAM NAME    COMMANDS  INPUT FILE       OUPUT FILE
------------------------------------------------------------------------------
python program_name.py +t +v -T6 < test_input.txt > test_output.txt
------------------------------------------------------------------------------
To break down what each part does, PYTHON is the Terminal or Powershell command
to run python. PROGRAM NAME is the name of the program being run. COMMANDS are
the commands you wish to run and apply to the file; in this case +t, +v and -T6.
INPUT FILE is directed to the program using "<" and the file name you want to
change. OUTPUT FILE saves the changes to an existing file, or new file, of your
choice. Please note that if you do not provide an OUTPUT FILE, the changes will
be printed to the screen but not saved.

==ADDITIONAL NOTES==
If you apply +t and +v to a file, and then apply -t and -v to the resulting
output, they should produce visually identical files.
    """)
    exit(0)

def error(error_code, user_input):
    """
    (F)unction:
    (I)nput:
    (R)eturn:
    """
    # each code represents a different error code
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

def main():
    error_report = "" # blank error report
    valid_help = "-help"
    ratio = RATIO_DEFAULT # sets ratio to default: 4

    # looks for incompatible arguments or -help first
    if ("-t" in sys.argv) and ("+t" in sys.argv):
        error_report += error("BT", None) + '\n'
    if ("-v" in sys.argv) and ("+v" in sys.argv):
        error_report += error("BV", None) + '\n'
    for arg in sys.argv:
        if (arg.upper() == "-HELP") and (len(sys.argv) == 2):
            help_text()
        elif (arg.upper() == "-HELP") and (len(sys.argv) != 2):
            error_report += error("HP", None)
    # starts looping through the file and applying conditions as encountered
    line = getInput()
    while (line != EOF):
        line = getInput()
        for arg in sys.argv:
            if (arg in sys.argv[0]): # skips first argument
                pass
            elif ("-T" in arg):
                ratio, error_report = upper_t(arg)
            elif (arg == "-v"):
                line = negative_v(line)
            elif (arg == "-t"):
                line = negative_t(line, ratio)
            elif (arg == "+t"):
                line = positive_t(line, ratio)
            elif (arg == "+v"):
                line = positive_v(line)
            elif (len(sys.argv) <= 1): # if the file is the only argument
                print(line) # copy input to output
            else:
                error_report += error("UA", arg) + '\n'
        # checks whether or not an error was encountered
        # if an error occurred, prints all errors and exits program
        if error_report != "":
            print("The following errors have occurred:")
            print(error_report)
            print("""
------------------------------------------------------------------------------
COMMAND     CHANGE
------------------------------------------------------------------------------
+t          -replaces prefix sequences of spaces of length T with a single tab
-t          -replaces prefix tabs with sequences of T spaces
-T<integer> -the <integer> defines the space-to-tab ratio, T (default=4)
+v          -changes all spaces, tabs, and newlines to printable characters
-v          -reverses the changes made by +v
-help       -prints out help text if -help is the only argument
------------------------------------------------------------------------------
Please note that the following arguments cannot be used together:
+t and -t cannot be passed as arguments together
+v and -v cannot be passed as arguments together
            """)
            exit(0)
        # if an error did not occur, prints each line with changes made
        else:
            print(line)

main()
