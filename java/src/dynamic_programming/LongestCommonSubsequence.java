package dynamic_programming;

public class LongestCommonSubsequence {

    private static final int NIL = -1;
    private static final int MAX_VALUE = 10;

    public static int[][] state = new int[MAX_VALUE+1][MAX_VALUE+1];

    // initialize the members of the state table to be default value of NIL (-1)
    static {
        for (int i = 0; i <= MAX_VALUE; i++) {
            for (int j = 0; j <= MAX_VALUE; j++) {
                state[i][j] = NIL;
            }
        }
    }

    /**
     * 
     *
     * Naive implementation not taking into account overlapping subproblems
     *
     * @param x First sequence to compare
     * @param y Second sequence to compare
     * @param m Length of first sequence
     * @param n Length of second sequence
     * @return The length of the longest common subsequence
     */
    public static int naiveLCSP(char[] x, char[] y, int m, int n) {
        // base case
        if (m == 0 || n == 0)
            return 0;

        if (x[m-1] == y[n-1])
            return 1 + naiveLCSP(x, y, m-1, n-1);
        else
            return Math.max(naiveLCSP(x, y, m, n-1), naiveLCSP(x, y, m-1, n));
    }

    /**
     * 
     *
     * Tabulated implementation, taking into account overlapping subproblems
     * @param x First sequence to compare
     * @param y Second sequence to compare
     * @param m Length of first sequence
     * @param n Length of second sequence
     * @return The length of the longest common subsequence
     */
    public static int tabulatedLcsp(char[] x, char[] y, int m, int n) {
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0)
                    state[i][j] = 0;
                else if (x[i-1] == y[j-1]) {
                    state[i][j] = 1 + state[i-1][j-1];
                } else
                state[i][j] = Math.max(state[i][j-1], state[i-1][j]);
            }
        }
        return state[m][n];
    }

    public static void main(String[] args) {
        String s1 = "SASHA";
        String s2 = "AHSAS";

        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();
        int m = c1.length;
        int n = c2.length;

        String result = String.format("Length of LCSP for %s and %s is %d", s1, s2, tabulatedLcsp(c1, c2, m, n));
        System.out.println(result + '\n');

        // show the rest of the state table
        StringBuilder builder = new StringBuilder();
        char newline = '\n';
        char space = ' ';
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <=n; j++) {
                builder.append(state[i][j]);
                builder.append(space);
            }
            builder.append(newline);
        }
        System.out.println("Tabulated result:");
        System.out.println(builder.toString());
    }
}
