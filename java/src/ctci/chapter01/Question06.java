package ctci.chapter01;

public class Question06 {

    /*
     * The rotation can be performed in layers, where you perform a cyclic
     * swap on the edges on each layer. In the first for loop, we rotate
     * the first layer (outermost edges). We rotate the edges by doing a
     * four-way swap first on the corners, then on the element clockwise
     * from the edges, then on the element three steps away. Once the
     * exterior elements are rotated, we then rotate the interior region’s
     * edges.
     */
    public static void rotateMatrix(int[][] matrix, int n) {
        for (int layer = 0; layer < n / 2; ++layer) {
            int first = layer;
            int last = n - 1 - layer;
            for (int i = first; i < last; ++i) {
                int offset = i - first;
                int top = matrix[first][i]; // save top

                // left -> top
                matrix[first][i] = matrix[last - offset][first];

                // bottom -> left
                matrix[last - offset][first] = matrix[last][last - offset];

                // right -> bottom
                matrix[last][last-offset] = matrix[i][last];

                // top -> right
                matrix[i][last] = top;
            }
        }
    }

    // Driver
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int n = matrix.length;
        rotateMatrix(matrix, n);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println();

        /* ------------------------------------------- */

        int [][] newMatrix = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}
        };

        int n2 = newMatrix.length;
        rotateMatrix(newMatrix, n2);

        for (int i = 0; i < n2; i++) {
            for (int j = 0; j < n2; j++) {
                System.out.print(newMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
