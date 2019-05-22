package sorting;

import java.lang.*;
import java.util.Arrays;

public class ZigzagSort {

    /**
     * Swap the integers at position i and j in the given array.
     *
     * @param arr The array to be modified.
     * @param i First position.
     * @param j Second position.
     */
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /**
     * Given an array of distinct elements, rearrange the elements of array in
     * zig-zag fashion in O(n) time
     *
     * @param arr The array to be zigzag sorted
     */
    public static void sort(int arr[]) {
        boolean compareLessThan = true;

        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] < arr[i+1]) {
                if (!compareLessThan) {
                    swap(arr, i, i+1);
                }
            } else {
                if (compareLessThan) {
                    swap(arr, i, i+1);
                }
            }
            compareLessThan = !compareLessThan;
        }
    }

    //Driver
    public static void main(String[] args) {
        int[] arr = {4, 3, 7, 8, 6, 2, 1};

        // Time complexity: O(n)
        // Auxiliary Space: O(1)
        sort(arr);

        System.out.println(Arrays.toString(arr));
    }
}