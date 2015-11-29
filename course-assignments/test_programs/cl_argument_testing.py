args = input("Please enter your arguments: ")
"""
Neither solves the problem of someone writing multiple characters after the
appropriate stopping point
"""

def check_condition(test_cond):
    value = None
    int_validity = False
    for char in test_cond[0]: # this is bad form. For loop iterates through a list, but the list here is one char.
        if (char == "+" or char == "-"):
            value = char
        else:
            return "Error. Invalid character."
    for char in test_cond[1]:
        if (char == "t" or char == "v"):
            value += char
        elif (char == "T"):
            value += char
            int_validity = True
        else:
            return "Error. Invalid operator."
    for char in test_cond[2]:
        if int_validity == True:
            if 2 <= int(char) <= 8:
                value += char
            else:
                return "The -T qualifier must be immediately followed by an integer: %s" % (char)
        else:
            return "Only the -T argument takes integers"
    return value

def check_validity_improved(arg):
    value = None
    int_validity = False
    if arg[0] == "+" or arg[0] == "-":
        value = arg[0]
        print(value)
    else:
        return "Error. Invalid character."
    if arg[1] == "t" or arg[1] == "v":
        value += arg[1]
        print(value)
    elif arg[1] =="T":
        value += arg[1]
        int_validity = True
        print(value, int_validity)
    else:
        return "Error. Invalid operator."
    if int_validity == True:
        if 2 <= int(arg[2]) <= 8:
            value += arg[2]
            print(value)
        elif int(arg[2]) < 2 or int(arg[2]) > 8:
            return "The -T qualifier must be immediately followed by an integer: %s" % (arg[2])
        else:
            value += 4
            print(value)
    elif int_validity == False:
        pass
    else:
        return "Something went wrong"

    return value

test1 = check_validity_improved(args)
test2 = check_condition(args)
print (test1)
print (test2)
