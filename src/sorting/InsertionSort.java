package sorting;

import java.utiil.*;
import java.lang.*;

public class InsertionSort {

    /**
     * Sorting algorithm that uses insertion sort to order the supplied array.
     *
     * @param arr The array to be sorted.
     */
    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i-1;

            /* Move elements of arr[0,..,i-1], that are greater than key,
            to one position ahead of their current position */
            while (j >= 0 && arr[j] > key) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = key;
        }
    }

    /**
     * Create a string representation of an integer array.
     *
     * @param arr The array to print.
     * @return A string represention of an integer array.
     */
    public static String printArray(int[] arr) {
        StringBuilder sb = new StringBuilder();
        sb.append('[');
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i] + " ");
        }
        sb.deleteCharAt(sb.length() - 1);
        sb.append(']');
        return sb.toString();
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 25, 5, 6};

        // insertion sort of array
        sort(arr);
        System.out.println(printArray(arr));
    }
}