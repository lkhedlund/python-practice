import sys

HEADER = """
==HELP DOCUMENT==
Indentation and Space Formatter by Lars Hedlund

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
------------------------------------------------------------------------------
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
Bugs: None known
Version: 1.0
"""

# Global Constants
EOF = chr(4)            # A standard End-Of-File character

TAB_CHAR = chr(187)     # A ">>" character in the extended ascii set
                        #   Used to make a tab character visible.
SPACE_CHAR = chr(183)   # A raised dot character in the extended ascii set
                        #   Used to make a space character visible
NEWLINE_CHAR = chr(182) # A backwards P character in the extended ascii set
                        #   Used to make a newline character visible
RATIO_DEFAULT = 4       # The default space-to-tab ratio

EMPTY = ""              # Used to initialize new strings as blank

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
        return RATIO_DEFAULT, EMPTY
    elif 2 <= int(arg[2]) <= 8: # checks that integer is within defined range
        ratio = int(arg[2])
        return ratio, EMPTY
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
    tabbed_line = EMPTY
    new_line = EMPTY
    trailing_sp = EMPTY

    # if the line is long enough, look for a tab to preserve trailing spaces
    if chr(9) in lead_line:
        # preserved spaces
        trailing_sp = lead_line[len(lead_line.rstrip(chr(32))):lead_len]
        # first replace the spaces with tabs
        lead_line = lead_line.replace(tab_length, chr(9))
        #then, to remove internal spaces, create only tabs
        for ch in lead_line:
            if ch == chr(9):
                tabbed_line += ch
        # to remove internal spaces, create only tabs
        if trailing_sp >= tab_length:
            line = tabbed_line + line.lstrip()
            return line
        else:
            # if they weren't converted to tabs, add back.
            line = tabbed_line + trailing_sp + line.lstrip()
            return line
    # if there is no tab, just convert the line and return it
    else:
         # if the leading space isn't long enough to convert, return it
        if lead_len < len(tab_length):
            return line
        else:
            # if the leading space is long enough, apply changes
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
    # length of the leading space
    lead_len = len(line) - len(line.lstrip())
    # splice of leading space
    lead_line = line[0:lead_len]
    tab_length = chr(32) * ratio
    new_line = EMPTY
    trailing_sp = EMPTY

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
    (F)unction: positive v replaces spaces, tabs, and newlines with characters
    (I)nput: string
    (R)eturn: string
    """
    new_line = EMPTY
    # check to see if the line is at the end of the file
    if line != EOF:
        for ch in line:
            if ch == chr(32):
                # replace spaces with a raised dot
                new_line += SPACE_CHAR
            elif ch == chr(9):
                 # replace tabs with '>>' and a tab to preserve formatting
                new_line += TAB_CHAR + chr(9)
            else:
                # add any additional characters
                new_line += ch
        # replaces the end of the line with the paragraph cahracter and adds \n to preserve format
        line = new_line.rstrip() + NEWLINE_CHAR
        return line
    else:
        return line

def negative_v(line):
    """
    (F)unction: negative v undoes the character replacement of positive v
    (I)nput: string
    (R)eturn: string
    """
    new_line = EMPTY
    #check to see if the line is at the end of the file
    if line != EOF:
        for ch in line:
            # replaces the raised dot with spaces
            if ch == SPACE_CHAR:
                new_line += chr(32)
            # does not add a tab to the new line since a tab was added in +v
            elif ch == TAB_CHAR:
                pass
             # does not add a \n since \n was added in +v
            elif ch == NEWLINE_CHAR:
                pass
            else:
                # adds all other characters
                new_line += ch
        return new_line
    else:
        return line

def help_text():
    """
    (F)unction: displays the help text if it is the only argument
    (I)nput: None
    (R)eturn: None
    """
    print(HEADER)
    exit(0)

def error(error_code, user_input):
    """
    (F)unction: Displays an error code based on the error that occurs
    (I)nput: string, string
    (R)eturn: string
    """
    # each code represents a different error
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
    error_report = EMPTY # blank error report
    valid_help = "-help"
    ratio = RATIO_DEFAULT # sets ratio to default: 4

    # determine whether the ratio will need to change
    if ("-T" in sys.argv):
        ratio, error_report = upper_t(arg)
    # looks for incompatible arguments or -help first
    if ("-t" in sys.argv) and ("+t" in sys.argv):
        error_report += error("BT", None) + '\n'
    if ("-v" in sys.argv) and ("+v" in sys.argv):
        error_report += error("BV", None) + '\n'
    # checks to see if the help argument is valid and the only argument
    for arg in sys.argv:
        if (arg.upper() == "-HELP") and (len(sys.argv) == 2):
            help_text()
        elif (arg.upper() == "-HELP") and (len(sys.argv) != 2):
            print(error("HP", None))
            print(ERROR_TEXT)
        else:
            pass
    # starts looping through the file and applying conditions as encountered
    line = EMPTY
    while (line != EOF):
        line = getInput()
        for arg in sys.argv:
            if (arg == sys.argv[0]): # skips first argument
                pass
            elif ("-T" in arg):
                pass # fixes a bug where -T was overwriting the error report
            elif (arg == "-v"):
                line = negative_v(line)
            elif (arg == "-t"):
                line = negative_t(line, ratio)
            elif (arg == "+t"):
                line = positive_t(line, ratio)
            elif (arg == "+v"):
                line = positive_v(line)
            else:
                error_report += error("UA", arg) + '\n'
        # checks whether or not an error was encountered
        # if an error occurred, prints all errors and exits program
        if error_report != EMPTY:
            print("The following errors have occurred:")
            print(error_report)
            print(ERROR_TEXT)
            exit(0)
            # if an error did not occur, prints each line with changes made
        else:
            print(line)

main()
