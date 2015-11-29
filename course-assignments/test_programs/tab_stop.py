def replace_space(string):
    result = ""
    default = 4
    i = 0
    while i < default:
        print("i = ", i)
        if string[i] == " ":
            result = result + string[i]
            i += 1
            print("result = ", result)
        elif string[i] == "\t":
            result.expandtabs[default] # expand tabs to the maximum (i.e. default)
    new_line = result.replace(result, "t") + string[i:]
    print(new_line)
"""
LOGIC: flawed. It looks for a tab in each character but, if a tab occurs later,
it will still add a space. It should.

I need if ANY OF THE CHARACTERS are a tab, expand tab to take up spaces.
"""
def replace_twice(string):
    result = ""
    default = 4
    tab_exists = False
    i = 0
    t_strip = len(string) - 4 # mimics lstrip
    if (t_strip) < default: # if range is less than the replacement range
        for i in range(t_strip): # for letters in a string
            if (string[i] == "\t") and (tab_exists == False): # if string at any index is tab
                result = string.expandtabs(t_strip) # expand tab to suck up spaces
                tab_exists = True
                print("result (<4, w/ tabs) = ", result)
            elif (string[i] == " ") and (tab_exists == False):
                result = result + string[i]  # ignore spaces
                print("result (<4, w/o tabs)= ", result)
            else:
                result = result #ignore character
    elif (t_strip) == default: # if range is equal to the replacement range
        for i in range(default): # for less in the replacement range
            if (string[i] == "\t") and (tab_exists == False): # if string at any index is tab
                result = string.expandtabs(t_strip) # expand tab to suck up spaces
                tab_exists = True
                print("result (<4, w/ tabs) = ", result)
            elif (string[i] == " ") and (tab_exists == False):
                result = result + string[i]  # ignore spaces
                print("result (<4, w/o tabs)= ", result)
            else:
                result = result #ignore character
    elif (t_strip) > default:



    new_line = result.replace(result, "p") + string[i:]
    print(new_line)

a_string = "    \ttest"
print(a_string)
print(replace_space(a_string))
print(replace_twice(a_string, 4))
