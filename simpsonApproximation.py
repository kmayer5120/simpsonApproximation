#Author: Kyle Mayer
#Simpson Approximation

'''
Process:
    -Get interval from lower and upper bounds
    -Use the interval to calculate midpoint interval
    -Calculate summation for left and right ends of rectangles
    -Use left and right end calculations to get trapezoids.
        Just average left and right.
    -Calculate summation of midpoint rectangles    
    -Take weighted average of trapezoids and midpoint rectangles. (2T+M)/3

    Result of Simpson approximation is an close approximation of an indefinite
    integral of some function. 


    Notes: 
    - I still need to define a neater way to switch functions. Very
    clunky and needs to be changed in multiple places as of this version.
    - Add ability for user to input bounds and desired equation?
    - Use matplotlib to show visual of area of indefinite integral?
    - GUI?
'''

import math

#define bounds
lowerBound = 1.0
upperBound = 3.0

#changing numIntervals increases precision
numIntervals = 1000000000

#find interval (b-a)/2
interval = (upperBound - lowerBound) / float(numIntervals)

#midpoint interval will always be half of interval used for L and R
mInterval = interval / 2.0 

#set starting points for each distributed summation
lStart = lowerBound
rStart = lowerBound + interval
mStart = lowerBound + mInterval

#init variables for each result
l = 0.0
r = 0.0
t = 0.0
m = 0.0
s = 0.0

#### Calculations
# Current function: 1/x

for i in range(0, numIntervals): 
    #dealing with L
    l += interval * (math.sqrt(lStart))
    #increment by interval
    lStart += interval
    
    #dealing with R
    if(rStart <= upperBound):
        r += interval * (math.sqrt(rStart))
        #increment by interval
        rStart += interval

#get average of L and R
t = (l + r) / 2

for i in range(0, numIntervals):
    #dealing with M
    if(mStart <= upperBound):
        m += interval * (math.sqrt(mStart))
        mStart += interval

#finally get simpson approximation using weighted average
s = ((2 * m) + t) / 3

print("         ----Results----")
print("Left end rectangle:  " + str(l))
print("Right end rectangle: " + str(r))
print("Trapezoid:           " + str(t)) 
print("Midpoint:            " + str(m))
print("Simpson:             " + str(s))
