#!/usr/bin/env python

"""
Author: David Ruffner
Date: 5/3/11

Script to calculate the prob of winning in a risk battle

"""

import pylab

nsides = 6
posvals = range(1,nsides+1)


poneoff = 0
ponedef = 0
for i in posvals:
    for j in posvals:
        for k in posvals:
                for m in posvals:
                    "going through all possible vals of dice"
                    odice = [i,j,k]
                    odice.sort()
                    odice.reverse()
                    #print odice
                    ddice = [m]
                    "determining who will win"
                    "Compare high die"
                    if odice[0] > ddice[0]:
                        poneoff = poneoff+1
                    else:
                        ponedef = ponedef+1
                    print i
print "poneoff"
print poneoff/pow(6.,4)

print "ponedef"
print ponedef/pow(6.,4)

"""
So the probability of winning with three vs two is .66 and of losing is .34
So it's really pretty bad to have those ones by themselves.
However, is it worth it to split up all your armies so that all your countries have two? I don't think so from experience

"""
