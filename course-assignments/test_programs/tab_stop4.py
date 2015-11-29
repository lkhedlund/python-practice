def space_replace(line, ratio):
    lead_len = len(line) - len(line.lstrip())
    lead_line = line[0:lead_len]
    tab_length = chr(32) * ratio
    tabbed_line = str()
    new_line = str()
    trailing_sp = str()

    print("Ratio: %r" % ratio)
    # checks to see if the line is long enough to replace
    if chr(9) in lead_line: # if the line is long enough, look for a tab to preserve trailing spaces
        trailing_sp = lead_line[len(lead_line.rstrip(chr(32))):lead_len] # preserved spaces
        print("Lead Line: %r" % lead_line)
        lead_line = lead_line.replace(tab_length, chr(9)) # first replace the spaces with tabs
        print("Lead Line: %r" % lead_line)
        for ch in lead_line: #then, to remove internal spaces, create only tabs
            if ch == chr(9):
                tabbed_line += ch
                print("Tabbed line: %r" % tabbed_line)
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
