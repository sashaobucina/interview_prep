package dynamic_programming;

import java.lang.*;
import java.util.*;

public class MinCostPath {

    public MinCostPath(){}

    public static int minCostPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0) {
            return -1;
        }

        return minCostPath(matrix, matrix[0].length - 1, matrix.length - 1);
    }

    private static int minCostPath(int[][] matrix, int x, int y) {
        if (x < 0 || y < 0) {
            return Integer.MAX_VALUE;
        } else if (x == 0 && y==0) {
            return matrix[x][y];
        } else {
            return matrix[x][y] +
                min(minCostPath(matrix, x-1, y-1),
                    minCostPath(matrix, x-1, y),
                    minCostPath(matrix, x, y-1)
                );
        }
    }

    private static int min(int x, int y, int z) {
        if (x < y) {
            return (x < z) ? x : z;
        } else {
            return (y < z) ? y : z;
        }
    }

    public static void main(String[] args) {
        int cost[][] = {{1, 2, 3},
                        {4, 8, 2},
                        {1, 5, 4}};

        System.out.println(minCostPath(cost));
    }
}