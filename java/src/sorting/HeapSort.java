// package sorting;
//
//import java.io.*;
//import java.util.*;
//import java.lang.*;
//
//public class HeapSort {
//
//    private static final int[] heap = {3, 3, 6, 4, 8, 9, 1, 100};
//
//    public static void sort() {
//        int n = heap.length;
//
//        buildMaxHeap(heap, n);
//        for (int i = n-1; i > 0; i--) {
//            int temp = heap[0];
//            heap[0] = heap[i];
//            heap[i] = temp;
//            maxHeapify(heap, 1, i); // one less item to worry about
//        }
//    }
//
//    private static void bulidMaxHeap(int[] arr, int heapSize) {
//        if (arr == null) {
//            throw new NullPointerException("Array is null!");
//        }
//
//        if (arr.length <= 0 || heapSize <= 0) {
//            throw new IllegalArgumentException("Params must be non-null");
//        }
//
//        if (heapSize > arr.length) {
//            heapSize = arr.length;
//        }
//
//        /* Start algorithm */
//        for (int i = heapSize/2; i > 0; i--) {
//            maxHeapify(arr, i, heapSize);
//        }
//
//    }
//
//    private static void maxHeapify(int[] arr, int ind, int heapSize) {
//        int left = 2*i;
//        int right = left + 1;
//        int largest = i;
//
//        if (left <= heapSize && arr[left - 1]  > arr[largest - 1]) {
//            largest = left;
//        }
//        if (right <= heapSize && arr[right - 1] > arr[largest - 1]) {
//            largest = right;
//        }
//        if (largest != i) {
//            swap(arr, largest, i);
//            maxHeapify(arr, largest, heapSize);
//        }
//    }
//
//    private static void swap(int[] arr, int ind1, int ind2) {
//        temp = arr[ind1];
//        arr[ind1] = arr[ind2];
//        arr[ind2] = temp;
//    }
//
//    public static void printArray() {
//        for (int i = 0; i < heap.length; i++) {
//            System.out.print(heap[i] + " ");
//        }
//        System.out.println();
//    }
//
//    public static void main(String[] args) {
//        // time complexity of O(nlogn)
//        // -> maxHeapify is O(logn)
//        // -> loop through entire heap which is O(n)
//        // therefore, total Big O complexity is O(nlogn)
//        HeapSort.sort();
//        HeapSort.printArray();
//    }
//}