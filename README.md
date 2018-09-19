# simpsonApproximation
Basic algorithm from my calculus 2 class that I wrote in Java, C++, and Python. 


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
