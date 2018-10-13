import java.io.*;
import java.lang.*;
import java.util.*;

public class Fibonacci {

    private static final int MAX_VALUE = 10000;
    private static final int NIL = -1;

    private static int[] states = new int[MAX_VALUE];

    /** static initializer of stateTable for dp implementation */
    static {
        states[0] = 1;
        states[1] = 1;
        states[2] = 1;
        for (int i = 3; i < MAX_VALUE; i++) {
            states[i] = NIL;
        }
    }

    /**
     * Naive implementation of Fibonacci using recursion.
     *
     * @param n The input of the fibonacci function.
     * @return The fibonacci of n.
     */
    public static int fib(int n) {
        return (n < 3) ? 1 : fib(n-1) + fib(n-2);
    }

    /**
     * The dynamic programming solution of Fibonacci, compromises space for
     * speed.
     *
     * @param n The input of the fibonacci function.
     * @return The fibonacci of n.
     */
    public static int fibDP(int n) {
        if (n+1 >= MAX_VALUE) 
            throw new IllegalArgumentException("Input size to big!");

        for (int i = 3; i <= n; i++) {
            states[i] = states[i-1] + states[i-2];
        }
        return states[n];
    }

    public static void main(String[] args) {
        System.out.println("Fibonacci of 6: " + fib(6));
        System.out.println("Fibonacci of 30 (DP solution) : " + fibDP(30));
    }
}