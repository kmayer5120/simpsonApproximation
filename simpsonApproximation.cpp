//Author: Kyle Mayer
//Simpson Approximation

/*
 * To compile:
 *      g++ simpsonApproximation.cpp -o simpsonApproximation
 *
 * To run:
 *      ./simpsonApproximation
 *
 *
 *  Notes:
 *      - See Python file for notes on what could be done to improve. 
*/


#include <iostream>
#include <math.h>

using namespace std;

int main() 
{
    double lowerBound = 1.0;
    double upperBound = 3.0;

    int numIntervals = 1000000000;

    double interval = (upperBound - lowerBound) / static_cast<double>(numIntervals);

    double mInterval = interval / 2.0;

    double lStart = lowerBound;
    double rStart = lowerBound + interval;
    double mStart = lowerBound + mInterval;

    double l = 0.0;
    double r = 0.0;
    double t = 0.0;
    double m = 0.0;
    double s = 0.0;

    //calculations

    for(int i = 0; i < numIntervals; i++)
    {
        //dealing with L
        l += interval * sqrt(lStart);
        lStart += interval;

        //dealing with L
        if(rStart <= upperBound)
        {
            r += interval * sqrt(rStart);
            rStart += interval;
        }
    }    

    //get average of L and R
    t = (l + r) / 2.0;

    for(int i = 0; i < numIntervals; i++)
    {
        if(mStart <= upperBound)
        {
            m += interval * sqrt(mStart);
            mStart += interval;
        }
    }

    s = ((2 * m) + t) / 3.0;

    cout.precision(20);
    cout << "\n         -----Results-----\n";
    cout << "Left end rectangle:     " << l << "\n";
    cout << "Right end rectangle:    " << r << "\n";
    cout << "Trapezoid:              " << t << "\n";
    cout << "Midpoint:               " << m << "\n";
    cout << "Simpson:                " << s << "\n";

}
