package leetcode;

import java.lang.*;
import java.util.*;

public class ReverseNum {

    public static int reverse(int x) {

        boolean isNegative = false;

        if (x < 0) {
            x = -x;
            isNegative = true;
        }

        int reversed = 0;
        int prevReversed = 0;
        while (x != 0) {
            int currDigit = (x % 10);
            reversed = (reversed * 10) + currDigit;

            if ((reversed - currDigit) / 10 != prevReversed) {
                System.out.println("Overflow!");
                return 0;
            }

            prevReversed = reversed;
            x = x / 10;
        }

        return isNegative ? -reversed : reversed;
    }

    public static void main(String[] args) {

        // Driver
        System.out.println(reverse(123));
        System.out.println(reverse(-123));
        System.out.println(reverse(120));
        System.out.println(reverse(1245405));
    }

}