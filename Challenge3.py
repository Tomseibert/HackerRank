# 32 bit mask
mask = 4294967295

def bitflip(x):
    return int(x) ^ mask

# get number of values from stdin as listCount
listCount = int(raw_input())

if listCount in range (1,101):
    for i in range(0,listCount):
        value = raw_input()
        flipped = bitflip(value)
        print flipped
else:
    print "Bad count %d" % listCount

# check to make sure input is from 1 to 100
# loop from 0 to listCount

