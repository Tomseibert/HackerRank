__author__ = 'MonkeyBoy'

def palindrome(string):
    strLen = len(string)
    letters = {}
    odd = False
    if (strLen % 2) == 1:
        odd = True
    for char in string:
        if letters.has_key(char):
            letters[char] += 1
        else:
            letters[char] = 1

    oddcount = 0
    for keys,value in letters.iteritems():
        if (value % 2) == 1:
            oddcount += 1

    if oddcount == 1 and odd:
        return True
    if oddcount == 0:
        return True

    return False

string = raw_input()

found = palindrome(string)
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

if not found:
    print("NO")
else:
    print("YES")