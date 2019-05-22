package dynamic_programming;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class LongestIncreasingSubsequence {

    private static int maxRef;
    private static final int DEFAULT = 1;
    private static final int MAX_VALUE = 100;

    public static int[] state = new int[MAX_VALUE];

    static {
        for (int i = 0; i < MAX_VALUE; i++) {
            state[i] = DEFAULT;
        }
    }

    /**
     * Finding the longest increasing subsequence of numbers in the given
     * sequence
     *
     * The naive implementation without considering overlapping subproblems
     *
     * @param arr The sequence to be examined.
     * @param n The length of the sequence.
     * @return The length of the longest increasing subsequence.
     */
    private static int naiveImpl(int[] arr, int n) {
        // base case
        if (n == 1)
            return 1;

        // maxEndingHere is the length of LISP ending with arr[n-1]
        int res, maxEndingHere = 1;

        for (int i = 1; i < n; i++) {
            res = naiveImpl(arr, i);
            if (arr[i-1] < arr[n-1] && res + 1 > maxEndingHere)
                maxEndingHere = res + 1;
        }

        if (maxRef < maxEndingHere)
            maxRef = maxEndingHere;

        return maxEndingHere;
    }

    public static int naiveLisp(int[] arr, int n) {
        maxRef = 1;
        naiveImpl(arr, n);
        return maxRef;
    }

    public static int tabulatedLisp(int[] arr, int n) {
        int max = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i] && state[i] < state[j] + 1)
                    state[i] = state[j] + 1;
            }
        }

        for (int i = 0; i < n; i++) {
            if (max < state[i]) {
                max = state[i];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int[] arr = {10, 22, 9, 33, 21, 50, 41, 60};
        int n = arr.length;
        System.out.println("Longest increasing subsequence (naive recursive): " + naiveLisp(arr, n));

        int[] tabArr = {10, 22, 9, 33, 21, 50, 41, 60};
        int m = tabArr.length;
        System.out.println("Longest increasing subsequence (tabulated): " + tabulatedLisp(arr, n));
    }
}
