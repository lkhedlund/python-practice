argument = input("Test ")

def argument_checker(arg):
    valid = True
    int_required = False
    if ("+" or "-") in arg[0]:
        pass
    else:
        print("Qualifier's first character requires a '+' or '-': %s" % arg)
        valid = False
    if ("t" or "v") in arg[1]:
        pass
    elif "T" in arg[1]:
        int_required = True
    else:
        print("Unrecognized argument: %s" % arg)



print(argument_checker(argument))
