package dynamic_programming;

public class PossibleCombosSum {
    private static final int MAX_VALUE = 10000;
    private static final int NIL = -1;
    public static int[] state = new int[MAX_VALUE];

    static {
        for (int i = 0; i < MAX_VALUE; i++) {
            state[i] = NIL;
        }

        // initialize base states
        state[1] = 1; // 1
        state[2] = 1; // 1 1
        state[3] = 2; //  1 1 1   3
        state[4] = 3; // 1 1 1 1   1 3   3 1
        state[5] = 5; // 1 1 3   1 3 1   3 1 1   5   1 1 1 1 1
    }

    /**
     * Given 3 numbers {1, 3, 5}, we need to tell the total number of ways we
     * can form a number 'N' using the sum of the given three numbers.
     *
     * Solved using memoization technique: top-down
     *
     * @param n The value of the sum
     * @return The number of possible arrangements
     */
    public static int memoizationSolve(int n) {
        // base cases
        if (n < 0)
            return 0;
        if (n == 0)
            return 1;

        // checking if already calculated
        if (state[n] != -1)
            return state[n];

        // recursive solution: top-down
        return state[n] = memoizationSolve(n-1) + memoizationSolve(n-3) + memoizationSolve(n-5);
    }

    /**
     * Given 3 numbers {1, 3, 5}, we need to tell the total number of ways we
     * can form a number 'N' using the sum of the given three numbers.
     *
     * Solved using tabulation technique: bottom-up
     *
     * @param n The value of the sum
     * @return The number of possible arrangements
     */
    public static int tabulationSolve(int n) {
        // Base cases
        if (n < 0)
            return 0;
        if (n == 0)
            return 1;

        // iterative solution: bottom-up
        for (int i = 0; i <= n; i++) {
            if (i <= 5) {
                continue;
            }
            state[i] = state[i-1] + state[i-3] + state[i-5];
        }
        return state[n];
    }

    public static void main(String[] args) {
         System.out.println("Number of arrangements for 7 (memoization): " + memoizationSolve(8) + "\n");
        System.out.println("Number of arrangements for 7 (tabulation): " + tabulationSolve(7) + "\n");

        // check memoized states, should be filled in up to 
        for (int i = 0; i < 10; i++) {
            System.out.println("State[" + i + "] = " + state[i]);
        }
    }
}
