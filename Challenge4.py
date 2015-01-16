#challenge 4




# get list count
# validate list count
# get values
# validate values

def growCycles(x):
    x = int(x)
    # tree is planted in spring at 1 meter
    # next cycle is fall where it grows twice in size.
    treeSize = 1
    if x == 0:
        return treeSize
    if x > 60:
        print "Max Cycle is 60"
        return
    for cycle in range(1,x+1):
        if (cycle % 2) == 1:
        # odd
            treeSize *= 2
        else:
        # even
            treeSize += 1

    return treeSize


listCount = int(raw_input())

if listCount in range (1,11):
    for i in range(0, listCount):
        value = raw_input()
        grown = growCycles(value)
        print grown
else:
    print "Bad Value"



