import java.io;
import java.lang.*;
import java.util.*;

public class BubbleSort {

    public void sort(int[] arr) {
        int i, j;
        boolean swapped;
        int n = arr.length;
        for (i = 0; i < n-1; i++) {
            swapped = false;
            for (j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) {
                break;
            }
        }
    }

    public void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.print("\n");
    }

    public static void main(String[] args) {

    }
}   