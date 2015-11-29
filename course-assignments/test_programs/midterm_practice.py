print("Q1")
print(int(3.14) % 3)

print("Q2")
sum = 0
for i in range(3):
    for j in range(i):
        sum = sum + j
print(sum)

print("Q3")
x = 1/2
print(x)

print("Q4")
s = '*'
s = s + s
s = s + s + s
print(s)

print("Q5")
for i in range(5):
    if i != 2:
        print("X")

print("Q6")
for i in range(2):
    for j in range(4):
        x = 1
        print(x)

print("Q7")
num = 10 + 2 / 3 * 4
print(type(num))

print("Q9")
for i in range(2):
    for j in range(4):
        x = 1
    print(x)

print("Q10")
x = 5
y = 4
print(x // y)

print("Q11")
x = 3
if (x <= 5 or x % 2 == 0):
    print(x)
print(1)

print("Q12") # infinite loop!
"""
num = 5
while(num > 0):
    print(num)
    num = num + 1
"""

print("Q13")
for name in ['Chirp', 'Peep']:
    print(name)

print("Q14")
for name in range(0,10,2):
    print(name)

print("Q15")
"""
x = 0
for i in range(3):
    n = int(input())
    x = x + n
print(x)
"""

print("Written 1")

def concat(string1, string2):
    return str(string1) + str(string2)

print(concat("hello", "world"))
print(concat(1, 2))

print("Written 2")
def is_palindrome(s):
    p = ''
    for ch in range(len(s)-1, -1, -1):
        p += ''.join(s[ch])
    if s == p:
        return True
    else:
        return False

print(is_palindrome("level"))
print(is_palindrome("icerink"))
