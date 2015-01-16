# this is an exercise to calculated the maximum xor value between two numbers.

# 1 < L < R < 1000
#
# Example if L = 10 and R = 15
# 10 ^ 10 = 0
# 10 ^ 11 = 1
# need two loops
# First loop is L to R for X where X ^ Y
# Second loop is L to R for Y where X ^ Y



def  maxXor( l,  r):
    if (r < l or r > 1000 or l < 1):
        print "Error bad value"
        return

    maxX = 0
    for x in range (l,r+1):
        for y in range (l,r+1):
            if maxX < (x ^ y):
                maxX = x ^ y
    return maxX


_l = int(raw_input());
_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
