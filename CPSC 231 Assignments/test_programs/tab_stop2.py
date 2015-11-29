def space_replace(line, ratio):
    count = 0
    lead_len = len(line) - len(line.lstrip())
    lead_line = line[0:lead_len]
    new_line = ""
    tab_length = chr(32) * ratio
    print("Lead_len ", lead_len)
    print("Ratio ", ratio)
    print(".",tab_length,".")

    for ch in lead_line:
        while count < ratio:
            if ch == " ":
                count += 1
                print("Count ", count)

    if (tab_length) in lead_line:
        new_line = lead_line.replace(tab_length, chr(9)) + line.lstrip()
        print("%r" % new_line)
    else:
        print("%r" % line)

def space_replace(line, ratio):
    lead_len = len(line) - len(line.lstrip()) # length of the leading whitespace
    lead_line = line[0:lead_len] # splices the leading whitespace
    new_line = "" # empty string
    tab_length = chr(32) * ratio # number of spaces to be converted to tabs

    if (tab_length) in lead_line: # looks for the correct number of spaces
        new_line = lead_line.replace(tab_length, chr(9)) + line.lstrip() # if there, replace with tab
        return new_line
    else:
        return line # if not, no changes made


test_str = "  \tTEST"
print(space_replace(test_str, 2))
print(space_replace(test_str, 4))
print(space_replace(test_str, 6))
print(space_replace(test_str, 8))
