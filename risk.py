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
        for k in posvals:
            for l in posvals:
                for m in posvals:
                    # going through all possible vals of dice"
                    odice = [i,j,k]
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
                    # print i
print ''
print """Calculation of risk battle odds. General case where offense has more
than three armies and defense has more than two:"""
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "Probability of defense losing two armies:"
print ptwooff/pow(6.,5)

print "Probability of offense losing two armies:"
print ptwodef/pow(6.,5)

print "Probability of both losing a single army:"
print psplits/pow(6.,5)
