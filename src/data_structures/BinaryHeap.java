
import java.io.*;
import java.lang.*;
import java.util.*;

public class BinaryHeap {

    private int numChildren = 2;
    private int heapSize;
    private int[] heap;

    public BinaryHeap(int maxCapacity) {
        this.heapSize = 0;
        this.heap = new int[maxCapacity];
        Arrays.fill(this.heap, -1);
    }

    public boolean isEmpty() {
        return (this.heapSize == 0);
    }

    public boolean isFull() {
        return (heapSize == this.heap.length);
    }

    public void emptyHeap() {
        this.heapSize = 0;
    }

    public int getParent(int i) {
        return heap((i - 1) / numChildren);
    }

    public int getKthChild(int i, int k) {
        return (numChildren * i) + k;
    }

    public void insert(int value) {
        if (isFull()) {
            throw NoSuchElementException("The heap is full");
        }
        heap[heapSize++] = x;
        heapifyUp(heapSize - 1);

    }

    public int findMin() {
        if (isEmpty()) {
            throw new NoSuchElementException("The heap is empty");
        }
        return this.heap[0];
    }

    public int deleteMin() {
        int keyItem = heap[0];
        delete(0);
        return keyItem;
    }

    public int delete(int ind) {
        if (isEmpty()) {
            throw new NoSuchElementException("The heap is empty");
        }
        int keyItem = heap[ind];
        heap[ind] = heap[heapSize - 1];
        heapSize --;
        heapifyDown(ind);
        return keyItem;

    }

    private void minChild(int ind) {
        int bestChild = getKthChild(ind, 1);
        int k = 2;
        int pos = getKthChild(ind, k);

        
    }

    private void heapifyUp(int childInd) {
        int temp = heap[childInd];

        while (childInd > 0 && tmp < heap[getParent(childInd)]) {
            heap[childInd] = heap[getParent(childInd)];
            childInd = getParent(childInd);
        }
        heap[childInd] = temp;
    }

    private void heapifyDown(int ind) {
        int smallest = ind;
        int left = 2*ind;
        int right = 2*ind + 1;

        if (left < heapSize && heap[left] < heap[smallest]) {
            smallest = left;
        }

        if (right < heapSize && heap[right] < heap[smallest]) {
            smallest = right;
        }

        if (smallest != i) {
            int temp = arr[smallest];
            heap[smallest] = heap[i];
            heap[i] = temp;
        }
    }

    public void printHeap() {
        System.out.println("Heap = ");
        for (int i = 0; i < heapSize; i++) {
            System.out.print(heap[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {

    }
}