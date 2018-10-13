package dynamic_programming;

import java.util.*;
import java.lang.*;

public class KnapsackProblem {

    /**
     * Implementation of the 0/1 knapsack problem in which the objective is to
     * find the subset of elements in which the sum of the values is maximized
     * but the sum of the weights is less than the maximum weight the knapsack
     * can hold.
     *
     * @param weight The maximum weight the knapsack can hold.
     * @param weightTable The weights associated to each element.
     * @param values The values associated to each element.
     * @param n The number of elements.
     * @return The maximum subset value of elements that is less than the
     *          maximum weight the knapsack can hold.
     */
    public static int knapsack(int W, int[] weightTable, int[] values, int n) {
        int[][] stateTable = new int[n+1][W+1];

        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= W; w++) {
                if (i == 0 || w == 0)
                    stateTable[i][w] = 0;
                else if (weightTable[i-1] > w)
                    stateTable[i][w] = stateTable[i-1][w];
                else 
                    stateTable[i][w] = Math.max(stateTable[i-1][w],
                            values[i-1] + stateTable[i-1][w-weightTable[i-1]]);
            }
        }
        return stateTable[n][W];
    }

    public static void main(String[] args) {
        int[] weightTable = {10, 20, 30};
        int[] values = {60, 100, 120};

        System.out.println("Max value: " + knapsack(50, weightTable, values, 3));
    }
}