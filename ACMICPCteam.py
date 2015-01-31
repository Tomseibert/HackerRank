__author__ = 'tom'

import itertools

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

def maxTeams(peopleList,maxTopic):

    count = len(peopleList)

    teams = 0

    for x,y in itertools.combinations(peopleList,2):
            maxTop = int(x,2) | int(y,2)
            bitsCount = bin(maxTop).count("1")
            if bitsCount == maxTopic:
                teams += 1

    return teams

# Main

# get total number of people and topics
inBuf = raw_input()
(people,topics) = inBuf.split()

peopleList = [raw_input() for _ in range(0,int(people))]
peopleList.sort()
#print peopleList
maxTop = maxTopics(peopleList)
teams = maxTeams(peopleList,maxTop)

print maxTop
print teams