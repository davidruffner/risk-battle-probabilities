#!/usr/bin/env python

"""
Author: David Ruffner
Date: 5/3/11

Script to calculate the prob of winning in a risk battle

"""

import pylab

nsides = 6
posvals = range(1,nsides+1)


ptwooff = 0
ptwodef = 0
psplits = 0
for i in posvals:
    for j in posvals:
        for l in posvals:
                for m in posvals:
                    # going through all possible vals of dice"
                    odice = [i,j]
                    odice.sort()
                    odice.reverse()
                    #print odice
                    ddice = [l,m]
                    ddice.sort()
                    ddice.reverse()
                    # determining who will win"
                    # Compare high die"
                    if odice[0] > ddice[0]:
                        ohigh = 1
                    else:
                        ohigh = 0
                    if odice[1] > ddice[1]:
                        olow = 1
                    else:
                        olow = 0
                    if olow and ohigh:
                        ptwooff = ptwooff+1
                    elif not olow and not ohigh:
                        ptwodef = ptwodef+1
                    else:
                        psplits = psplits+1

print ''
print """Calculation of risk battle odds. The case where offense and
defense only have two armies. The offensive probabilities go way down
compared to the general case:"""
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "Probability of defense losing two armies:"
print ptwooff/pow(6.,4)

print "Probability of offense losing two armies:"
print ptwodef/pow(6.,4)

print "Probability of both losing a single army:"
print psplits/pow(6.,4)
