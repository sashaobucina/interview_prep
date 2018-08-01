package leetcode;

import java.lang.*;

public class SubArraySum {

    public static int[] subarraySum(int [] arr, int sum) {

        int currSum = arr[0];
        int startIndex = 0;

        for (int i = 1; i <= arr.length; i++) {

            if (currSum > sum) {
                while (currSum > sum) {
                    currSum = currSum - arr[startIndex];
                    startIndex += 1;
                }
            }
            if (currSum == sum) {
                return new int[] {startIndex, i-1};
            }

            if (i < arr.length) {
                currSum += arr[i];
            }
        }
        System.out.println("Subarray with given sum was not found");
        return null;
    }

    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void main(String[] args) {
        // Driver
        int[] arr = new int[] {3, 2, 1, 18, 12};
        printArray(subarraySum(arr, 2)); // hope it works
    }

}