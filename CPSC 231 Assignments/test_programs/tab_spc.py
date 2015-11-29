def space_replace(line, ratio):
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

    print("Ratio: %r" % ratio)
    # check to see if there is a tab
    if chr(9) not in lead_line:
        # if there isn't a tab, return the line
        return line
    else:
        for ch in lead_line:
            if ch == chr(32):
                count += 1
                print("Count: %r" % count)
            elif (ch == chr(9)) and (count < len(tab_length)):
                new_line += tab_length
                print("Count: %r" % count)
                count = 0
                print("count < len(tab_length)")
                print("Newline: %r" % new_line)
            elif (ch == chr(9)) and (count >= len(tab_length)):
                new_line += (chr(32) * count) + tab_length
                print("Count: %r" % count)
                count = 0
                print("count >= len(tab_length)")
                print("Newline: %r" % new_line)
            else:
                print("Error")
        trailing_sp = chr(32) * count
        line = new_line + trailing_sp + line.lstrip()
        return line

print("------String 1------")
test_str = "      TEST"
print("%r" % space_replace(test_str, 2))
print("%r" % space_replace(test_str, 4))
print("%r" % space_replace(test_str, 6))
print("%r" % space_replace(test_str, 8))
print("------String 2-------")

test_str = "  \t    TEST"
print("%r" % space_replace(test_str, 2))
print("%r" % space_replace(test_str, 4))
print("%r" % space_replace(test_str, 6))
print("%r" % space_replace(test_str, 8))
print("------String 3-------")

test_str = "    \t  TEST"
print("%r" % space_replace(test_str, 2))
print("%r" % space_replace(test_str, 4))
print("%r" % space_replace(test_str, 6))
print("%r" % space_replace(test_str, 8))
print("----------------------")

"""
BUGS
problem with the output where "    \t  TEST" is not removing the leading spaces.
Basically, if the line cannot replace the leading spaces it should just print the tab.
"""
