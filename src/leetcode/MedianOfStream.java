package leetcode;

import java.util.*;
import java.lang.*;

public class MedianOfStream {

    
    public static void buildMaxHeap(int[] arr, int heapSize) {
        int depth = (heapSize - 1) / 2;
        for (int i = depth; i >= 0; i--) {
            maxHeapify(arr, i, heapSize);
        }
    }

    public static void maxHeapify(int[] arr, int index, int heapSize) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        // find the largest
        int largest = i;

        if (left < heapSize && arr[left] > arr[i]) {
            largest = left;
        }

        if (right < heapSize && arr[right] > arr[i]) {
            largest= right;
        }

        // if largest value has changed, need to swap values
        if (largest != i) {
            swap(arr, i, largest);
            // handle the affected sub-tree
            maxHeapify(arr, largest, heapSize);
        }

    }

    public static void buildMinHeap(int[] arr, int heapSize) {
        int depth = (heapSize-1) / 2;
        for (int i = depth; i>=0;i--) {
            minHeapify(arr, i, heapSize);
        }
    }

    public static void minHeapify(int[] arr, int i, int heapSize) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        // find the smallest
        int smallest = i;

        if (left < heapSize && arr[left] < arr[i]) {
            largest = left;
        }

        if (right < heapSize && arr[right] < arr[i]) {
            largest = right;    
        }

        // if largest value has changed, need to swap values
        if (largest != i) {
            swap(arr, i, largest);
            // handle the affected sub-tree
            minHeapify(arr, largest, heapSize);
        } 
    }

    public static void swap(int[] arr, int a, int b) {
        if (a == b) return;
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        int[] minHeap = new int[n];
        int[] maxHeap = new int[n];
        int minHeapSize = 0;
        int maxHeapSize = 0;

        float currentMedian = 0;

        for (int a_i = 0; a_i < n; a_i++) {
            arr[a_i] = in.nextInt();
            if (arr[a_i] < currentMedian) {
                maxHeap[maxHeapSize++] = arr[a_i];
                if (maxHeap[maxHeapSize - 1] > 0) {
                    swap(maxHeap, maxHeapSize-1, 0);
                }
            } else {
                minHeap[minHeapSize++] = arr[a_i];
                if (minHeap[minHeapSize - 1] < minHeap[0]) {
                    swap(minHeap, minHeapSize-1, 0);
                }
            }

            if (Math.abs(maxHeapSize - minHeapSize) > 1) {
                if (maxHeapSize > minHeapSize) {
                    swap(maxHeap, maxHeapSize - 1, 0);
                    minHeap[minHeapSize++] = maxHeap[--maxHeapSize];
                    swap(minHeap, 0, minHeapSize - 1);
                    buildMaxHeap(maxHeap, maxHeapSize);
                } else {
                    swap(minHeap, minHeapSize - 1, 0);
                    maxHeap[maxHeapSize++] = minHeap[--minHeapSize];
                    swap(maxHeap, 0, maxHeapSize - 1);
                    buildMinHeap(minHeap, minHeapSize);
                }
            }

            // calculate the median
            if (minHeapSize == maxHeapSize) {
                currentMedian = (minHeap[0] + maxHeap[0]) / 2;
            } else if (maxHeapSize > minHeapSize) {
                currentMedian = maxHeap[0];
            } else {
                currentMedian = minHeap[0];
            }

            // print the current median on a new line
            System.out.println(currentMedian);
        }

    }

}