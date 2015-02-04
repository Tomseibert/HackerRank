__author__ = 'MonkeyBoy'




























# Main

# get total number of people and topics
inBuf = raw_input()
(jars,operations) = inBuf.split()

for _ in range(0,int(operations)):
    inBuf = raw_input()
    (startRange, endRange, candy) = inBuf.split()
    print "%d  %d  %d" % (int(startRange),int(endRange),int(candy))