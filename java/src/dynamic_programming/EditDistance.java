package dynamic_programming;

public class EditDistance {

    private static int min (int a, int b, int c) {
        if (a < b && a < c) {
            return a;
        } else if (b < a && b < c) {
            return b;
        } else {
            return c;
        }
    }

    /**
     * Find the minimum number of operations (remove, insert, replace) to
     * convert s1 to s2.
     *
     * Naive implementation without taking into account overlapping subproblems
     *
     * @param s1 The base string
     * @param s2 The string to compare to
     * @param m The length of the base string
     * @param n The length of the second string
     * @return The minimum number of operations to convert s1 to s2
     */
    public static int naiveEditDistance(String s1, String s2, int m, int n) {
        if (m == 0)
            return n;
        if (n == 0)
            return m;

        if (s1.charAt(m-1) == s2.charAt(n-1))
            return naiveEditDistance(s1, s2, m-1, n-1);

        return 1 + min(naiveEditDistance(s1, s2, m, n-1),       // Insert
                        naiveEditDistance(s1, s2, m-1, n),      // Remove
                        naiveEditDistance(s1, s2, m-1, n-1)   // Replace
        );
    }

    /**
     * Find the minimum number of operations (remove, insert, replace) to
     * convert s1 to s2.
     *
     * Implementation with tabulation
     *
     * @param s1 The base string
     * @param s2 The string to compare to
     * @param m The length of the base string
     * @param n The length of the second string
     * @return The minimum number of operations to convert s1 to s2
     */
    public static int editDistance(String s1, String s2, int m, int n) {
        int[][] state = new int[m+1][n+1];

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                // given first string is empty, only option to insert all chars from second string
                if (i==0)
                    state[i][j] = j;

                // same logic as above condition
                else if (j==0)
                    state[i][j] = i;

                else if (s1.charAt(i-1) == s2.charAt(j-1))
                    state[i][j] = state[i-1][j-1];

                else
                    state[i][j] = 1 + min(state[i-1][j],    // Insert
                                        state[i][j-1],      // Remove
                                        state[i-1][j-1]     // Replaces
                );
            }
        }
        return state[m][n];
    }

    // Driver
    public static void main(String[] args) {
        String s1 = "saturday";
        String s2 = "sunday";

        // naive implementation -> O(3^{n/m})
        System.out.println(
            "Edit distance (naive): " + naiveEditDistance(s1, s2, s1.length(), s2.length()));

        s1 = "state";
        s2 = "status";

        // implementation with tabulation/memoization -> O(m x n)
        System.out.println(
            "Edit distance (tabulation): " + editDistance(s1, s2, s1.length(), s2.length()));
    }
}
