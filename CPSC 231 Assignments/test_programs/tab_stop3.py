def space_replace(line, ratio):
    lead_len = len(line) - len(line.lstrip())
    lead_line = line[0:lead_len]
    tab_length = chr(32) * ratio
    tabbed_line = str()
    new_line = str()
    trailing_sp = str()

    print("Lead_len ", lead_len)
    print("Ratio ", ratio)
    print("Tab Length: %r" % tab_length)


    # Remove trailing spaces for use after conversion.
    if chr(9) in lead_line:
        trailing_sp = lead_line[len(lead_line.rstrip(chr(32))):lead_len]

    new_line = lead_line.replace(tab_length, chr(9))

    # Remove internal spaces (i.e. tab stop)
    for ch in new_line:
        if ch == chr(9):
            tabbed_line += ch
            
    if trailing_sp == tab_length:
        line = tabbed_line + chr(9) + line.lstrip()
        return line
    else:
        line = tabbed_line + trailing_sp + line.lstrip()
        return line



test_str = "      TEST"
print(space_replace(test_str, 2))
print(space_replace(test_str, 4))
print(space_replace(test_str, 6))
print(space_replace(test_str, 8))
