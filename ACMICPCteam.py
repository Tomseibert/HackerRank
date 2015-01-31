__author__ = 'tom'

maxTopics = 500
maxPeople = 500


# how many teams can know max topics
def teamCount():
    pass

# what is max topics knowable
def maxTopics(peopleList):
    # this is a bad way to compare the two. Need to check all against all.
    # this could result in a very long processing time
    bitsOn = 0
    count = len(peopleList)
    for i in range(0,count):
        for j in range(0,count):
            maxTop = int(peopleList[i],2) | int(peopleList[j],2)
            bitsCheck = bin(maxTop).count("1")
            if bitsCheck > bitsOn:
                bitsOn = bitsCheck



    # need to count the on bits not the total number..
    return bitsOn

# Main

# get total number of people and topics
inBuf = raw_input()
(people,topics) = inBuf.split()

peopleList = [raw_input() for _ in range(0,int(people))]
peopleList.sort()
#print peopleList
max = maxTopics(peopleList)

print max