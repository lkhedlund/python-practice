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

def string_modification():
    stop = False
    while stop == False:
        line = getInput()
        if line == EOF:
            stop = True
        else:
            print("Original:")
            print(line)
            rem_tab = line.lstrip(chr(9))
            print("Tabs removed:")
            print(rem_tab)
            sp_replace = line.replace(chr(32), chr(183))
            print(sp_replace)
            print("----------------")


string_modification()
