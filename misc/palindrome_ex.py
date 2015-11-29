# Instructions: Check whether or not a sentence is a palindrome.

def palindrome_one(sentence):
    reverse = ""
    for ch in sentence:
        reverse = ch + reverse # So elegant.
        # Just reverse the order you add the characters in.
    if reverse == sentence:
        return True
    else:
        return False

def palindrome_two(sentence):
    reverse = ""
    for ch in range(len(sentence)-1, -1, -1): # Less elegant, but correct.
        #loops backwards through the sentence and joins the results together.
        reverse += "".join(sentence[ch])
    if reverse == sentence:
        return True
    else:
        return False

def palindrome_three(sentence):
    if sentence == sentence[::-1]: # also 'loops' through the sentence backwards
    # creates a comparable temporary string that is the reverse.
        return True
    else:
        return False

print(palindrome_one("level"))
print(palindrome_one("completed"))

print(palindrome_two("level"))
print(palindrome_two("completed"))

print(palindrome_three("level"))
print(palindrome_three("completed"))
