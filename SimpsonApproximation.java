//Author: Kyle Mayer
//Simpson Approximation

/*
 * Notes:
 *      See Python file for notes on what could be done to 
 *      improve upon this code.
*/

import java.lang.Math;

public class SimpsonApproximation
{
    public static void main(String[] args)
    {
        double lowerBound = 1.0;
        double upperBound = 3.0;

        int numIntervals = 1000000000;

        double interval = (upperBound - lowerBound) / (double)numIntervals;

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
            l += interval * Math.sqrt(lStart);
            lStart += interval;

            //dealing with L
            if(rStart <= upperBound)
            {
                r += interval * Math.sqrt(rStart);
                rStart += interval;
            }
        }    

        //get average of L and R
        t = (l + r) / 2.0;

        for(int i = 0; i < numIntervals; i++)
        {
            if(mStart <= upperBound)
            {
                m += interval * Math.sqrt(mStart);
                mStart += interval;
            }
        }

        s = ((2 * m) + t) / 3.0;

        System.out.println("\n         -----Results-----");
        System.out.printf("\nLeft end rectangle:    %.16f", l);
        System.out.printf("\nRight end rectangle:   %.16f", r);
        System.out.printf("\nTrapezoid:             %.16f", t);
        System.out.printf("\nMidpoint:              %.16f", m);
        System.out.printf("\nSimpson:               %.16f \n", s);

    }




}

