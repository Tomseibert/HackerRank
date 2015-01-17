# use ord and chr to change values

maxString = 10000


def palindrome(string):
    changes = 0
    strLen = len(string)
    if strLen > maxString:
        print "Error"
        return
    if strLen % 2 == 1:
        # odd don't change middle
        partLen = (strLen -1) / 2
        leftPart = list(string[0:partLen:1])
        rightPart = string[partLen+1::1]
        rightPart = list(rightPart[::-1])
        mid = string[partLen:partLen+1:1]
        print "Left %s" % leftPart
        print "Right %s" % rightPart
        print "Mid: %s" % mid
    else:
        # even no middle to change
        partLen = strLen / 2
        leftPart = list(string[0:partLen:1])
        rightPart = string[partLen::1]
        rightPart = list(rightPart[::-1])
        print "Left %s" % leftPart
        print "Right %s" % rightPart
    for i in range(0,partLen):
        if leftPart[i] == rightPart[i]:
            continue
        if leftPart[i] > rightPart[i]:
            diff = ord(leftPart[i]) - ord(rightPart[i])
            changes += diff
            leftPart[i] = chr(ord(leftPart[i])-diff)
        if leftPart[i] < rightPart[i]:
            diff = ord(rightPart[i]) - ord(leftPart[i])
            rightPart[i] = chr(ord(rightPart[i])-diff)
            changes += diff

    return changes


#main

listCount = int(raw_input())

if listCount in range (1,11):
    for i in range(0, listCount):
        value = raw_input()
        changes = palindrome(value)
        print changes
else:
    print "Bad Value"