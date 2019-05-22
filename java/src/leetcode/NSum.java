package leetcode;

import java.util.*;
import java.lang.*;

/** Class that holds the implementation of various {N}Sum problems */
public class NSum {

    /**
     * Given an array S of n integers, are there elements a, b, c in S
     * such that a + b + c = 0? Find all unique triplets in the array which
     * gives the sum of zero.
     *
     * @param arr The array to be analyzed.
     * @return The solution set for 3Sum for this particular input array.
     */
    public static List<List<Integer>> threeSum(int[] arr) {
        Set<List<Integer>> solutionSet = new HashSet<>();

        if (arr == null || arr.length < 3) {
            return new ArrayList<>(solutionSet);
        }

        Arrays.sort(arr);

        for (int i = 0; i < arr.length - 2; i++) {
            int j = i+1;
            int k = arr.length - 1;

            while (j < k) {
                int threeSum = arr[i] + arr[j] + arr[k];
                if (threeSum == 0) {
                    List<Integer> solution = new ArrayList<>();
                    solution.add(arr[i]);
                    solution.add(arr[j]);
                    solution.add(arr[k]);
                    solutionSet.add(solution);

                    j++;
                    k--;

                    while (j<k && arr[j] == arr[j+1]) {
                        j++;
                    }
                    while (j<k && arr[k] == arr[k-1]) {
                        k--;
                    }
                } else if (threeSum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        return new ArrayList<>(solutionSet);
    }

    // Driver
    public static void main(String[] args) {
        int[] arr = {-1, 0, 1, 2, -1, -4};

        System.out.println("Solution set of 3Sum:");
        List<List<Integer>> result = threeSum(arr);
        for (List<Integer> solution : result) {
            System.out.println(solution.toString());
        }
    }
}