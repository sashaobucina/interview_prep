public class SelectionSort {

    public void sort(int[] arr) {

        int n = arr.length;
        int i, j;

        for (i = 0; i < n-1; i ++) {
            int min_idx = i;
            for (j = i+1; j < n; j++) {
                if (arr[j] < arr[min_idx]) {
                    min_idx = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
        }

    }

    public void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {

    }
}