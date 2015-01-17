# max string length
maxString = 100000
# max number of possible tests
maxTest = 10


def countDel(inStr):
    if len(inStr) > maxString:
        print "String too long"
        return
    first = True
    dels = 0
    for char in inStr:
        if first:
            lastChar = char
            first = False
            continue
        if lastChar == char:
            dels += 1
        lastChar = char
    return dels

listCount = int(raw_input())

if listCount in range (1,11):
    for i in range(0, listCount):
        value = raw_input()
        deleted = countDel(value)
        print deleted
else:
    print "Bad Value"