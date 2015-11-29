# Global Constants
EOF = chr(4)            # A standard End-Of-File character

TAB_CHAR = chr(187)     # A ">>" character in the extended ascii set
                        #   Used to make a tab character visible.
SPACE_CHAR = chr(183)   # A raised dot character in the extended ascii set
                        #   Used to make a space character visible
NEWLINE_CHAR = chr(182) # A backwards P character in the extended ascii set
                        #   Used to make a newline character visible
RATIO_DEFAULT = 4       # The default space-to-tab ratio

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
        line = new_line.rstrip() + NEWLINE_CHAR + '\n' # replaces the end of the line with the paragraph cahracter and adds \n to preserve format
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
    #check to see if the line is at the end of the file
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

line = "    \t\tThere is no reason this shouldn't work...or   is there.? "
new_line = positive_v(line)
print("%r" % new_line)
newer_line = negative_v(new_line)
print("%r" % newer_line)
