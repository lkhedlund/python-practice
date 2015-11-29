import sys

EOF = chr(4)

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

def space_replace(line, ratio):
    lead_len = len(line) - len(line.lstrip())
    lead_line = line[0:lead_len]
    tab_length = chr(32) * ratio
    tabbed_line = str()
    new_line = str()
    trailing_sp = str()

    if chr(9) in lead_line:
        trailing_sp = lead_line[len(lead_line.rstrip(chr(32))):lead_len]


    print("Lead_len ", lead_len)
    print("Ratio ", ratio)
    print("Tab Length: %r" % tab_length)
    print("Trailing Space: %r" % trailing_sp)

    new_line = lead_line.replace(tab_length, chr(9))
    print("New Line: %r" % new_line)
    for ch in new_line:
        if ch == chr(9):
            tabbed_line += ch
    print("Tab line: %r" % tabbed_line)
    line = tabbed_line + trailing_sp + line.lstrip()
    print("Final Line: %r" % line)

def main():
    ratio = 4
    firstArg = False

    if ("-t" and "+t") in sys.argv:
        #error_report += error("t", arg)
        pass
    elif ("-v" and "+v") in sys.argv:
        #error_report += error("v", arg)
        pass
    else:
        line = getInput()
        while (line != EOF):
            line = getInput()
            for arg in sys.argv:
                if firstArg:
                    firstArg = False
                elif ("+t" == arg):
                    print(space_replace(line, ratio))

main()
