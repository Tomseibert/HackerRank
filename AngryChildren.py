__author__ = 'MonkeyBoy'

#import time

def fairness(candies,totalPack,children):
    first = True
    for x in range(0,totalPack-children):
        diff = candies[x+(children-1)] - candies[x]
        if first:
            lowestDiff = diff
            first = False
        else:
            if lowestDiff > diff:
                lowestDiff = diff
    return lowestDiff


n = input()
k = input()

# timing
#start = time.time()
#
candies = [input() for _ in range(0,n)]
#
#lap = time.time()
#print "Load Time: %f" % (lap - start)

candies.sort()
#lap = time.time()
#print "Sort Time: %f" % (lap - start)

min_diff = fairness(candies,n,k)
#lap = time.time()
#print "Locate Time: %f" % (lap - start)

print min_diff
