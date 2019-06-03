package trees;

import java.util.*;

class Node {

    int value;

    int inOrderValue = -1;
    int postOrderValue = -1;
    int preOrderValue = -1;

    Node left;

    Node right;

    public Node() {
        this.left = null;
        this.right = null;
    }

    public Node(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public Node(int value, Node left, Node right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    @Override
    public String toString() {
        return this.value + " , preorder: " + this.preOrderValue + ", inorder: " + this.inOrderValue + ", postorder: " + this.postOrderValue + " ";
    }

}


public class BinaryTree {

    public Node head;

    private int num = 0;

    public BinaryTree(Node node) {
        this.head = node;
    }

    class PrevNode extends Node {
        Node root;

        public PrevNode() {
            root = null;
        }
    }

    public List<List<Integer>> zigzagTraversal(Node root) {
        List<List<Integer>> result = new ArrayList<>();

        // base case if root given is null
        if (root == null) {
            return result;
        }

        boolean leftToRight = true;
        Stack<Node> currentLevel = new Stack<>();
        Stack<Node> nextLevel = new Stack<>();
        currentLevel.push(root);

        ArrayList<Integer> element = new ArrayList<>();

        while (!currentLevel.isEmpty()) {
            Node currentNode = currentLevel.pop();
            element.add(currentNode.value);

            // add the children to the next level
            if (leftToRight) {
                if (currentNode.left != null) {
                    nextLevel.push(currentNode.left);
                }
                if (currentNode.right != null) {
                    nextLevel.push(currentNode.right);
                }
            }
            else {
                if (currentNode.right != null) {
                    nextLevel.push(currentNode.right);
                }
                if (currentNode.left != null) {
                    nextLevel.push(currentNode.left);
                }
            }

            if (currentLevel.isEmpty()) {
                leftToRight = !leftToRight;
                Stack<Node> temp = currentLevel;
                currentLevel = nextLevel;
                nextLevel = temp; // because currLevel is empty

                /* add to the resulting list */
                result.add(element);
                element = new ArrayList<>();
            }
        }
        return result;
    }

    public void inOrderTraversal(Node curr) {
        if (curr != null) {
            inOrderTraversal(curr.left);
            System.out.println(curr);
            inOrderTraversal(curr.right);
        }
    }

    public void preOrderTraversal(Node curr) {
        if (curr != null) {
            System.out.println(curr);
            preOrderTraversal(curr.left);
            preOrderTraversal(curr.right);
        }
    }

    public void postOrderTraversal(Node curr) {
        if (curr == null) return;
        postOrderTraversal(curr.left);
        postOrderTraversal(curr.right);
        System.out.println(curr);

    }

    /**
     * O(n) time complexity
     * @param rootNode
     * @param prevNode
     * @param startNodeValue
     * @return
     */
    private Node inOrderNextHelper(Node rootNode, PrevNode prevNode, int startNodeValue) {

        if (rootNode.right != null) {
            return inOrderNextHelper(rootNode.right, prevNode, startNodeValue);
        }

        // found next node inorder traversal
        if (rootNode.value == startNodeValue) {
            return prevNode.root;
        }

        if (rootNode.left != null) {
            return inOrderNextHelper(rootNode.left, prevNode, startNodeValue);
        }
        return null;
    }

    public Node inOrderNext(int targetNode) {
        return inOrderNextHelper(head, new PrevNode(), targetNode);
    }

    private Node postOrderNextHelper(Node root, int target) {
        if (target == root.value) {
            return null;
        }
        Node parent = findParent(head, target);
        if (parent.right == null || parent.right.value == target) {
            return parent;
        }

        Node currNode = parent.right;
        while (currNode.left != null || currNode.right != null) {
            if (currNode.left != null) {
                currNode = currNode.left;
            } else {
                currNode = currNode.right;
            }
        }
        return currNode;
    }

    public Node postOrderNext(int target) {
        return postOrderNextHelper(head, target);
    }

    private Node findParent(Node rootNode, int target) {
        if (head.value == target || rootNode == null) {
            return null;
        } else {
            if ((rootNode.left != null && rootNode.left.value == target)
                    || (rootNode.right != null && rootNode.right.value == target)) {
                return rootNode;
            } else {
                Node leftSearch = findParent(rootNode.left, target);
                return (leftSearch != null) ? leftSearch : findParent(rootNode.right, target);
            }
        }
    }

    private void inOrderHelper(Node curr) {
        if (curr == null) return;

        inOrderHelper(curr.left);
        curr.inOrderValue = ++this.num;
        inOrderHelper(curr.right);

    }

    public void inOrderNumber() {
        inOrderHelper(head);
        this.num = 0;
    }

    private void postOrderHelper(Node curr) {
        if (curr == null) return;

        postOrderHelper(curr.left);
        postOrderHelper(curr.right);
        curr.postOrderValue = ++this.num;
    }

    public void postOrderNumber() {
        postOrderHelper(head);
        this.num = 0;
    }

    private void preOrderHelper(Node curr) {
        if (curr == null) return;

        curr.preOrderValue = ++this.num;
        preOrderHelper(curr.left);
        preOrderHelper(curr.right);
    }

    public void preOrderNumber() {
        preOrderHelper(head);
        this.num = 0;
    }

    public boolean isBST() {
        return isBSTUtil(head, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private boolean isBSTUtil(Node curr, int min, int max) {
        // empty tree is still a binary search tree
        if (curr == null) {
            return true;
        }

        if (curr.value < min || curr.value > max) {
            return false;
        }

        return (isBSTUtil(curr.left, min, curr.value-1) &&
                isBSTUtil(curr.right, curr.value - 1, max));
    }

    public void add(int val) {
        /* wrapper function to add fromt the top */
        add(this.head, val);
    }

    public void depthFirstSearch() {

        // call wrapper function hidden from API
        if (this.head != null) {
            depthFirstSearch(this.head);
        }

    }

    public boolean hasPathSum(Node root, int sum) {
        if (root == null)
            return false;
        return hasPathSumHelper(root, sum);
    }

    private boolean hasPathSumHelper(Node node, int sum) {
        if (node == null) {
            return (sum == 0);
        } else {
            boolean ans = false;

            /* check both subtrees */
            int subsum = sum - node.value;
            if (subsum == 0 && node.left == null && node.right == null)
                return true;
            if (node.right != null)
                ans = ans || hasPathSumHelper(node.right, subsum);
            if (node.left != null)
                ans = ans || hasPathSumHelper(node.left, subsum);
            return ans;
        }
    }

    private void depthFirstSearch(Node root) {

        Stack<Node> stack = new Stack<>();
        stack.push(root);

        Node currNode;
        while (!stack.isEmpty()) {
            
            // add the children of the current node that was popped
            currNode = stack.pop();
            System.out.print(currNode.value + " ");

            if (currNode.right != null) {
                stack.push(currNode.right);
            }

            if (currNode.left != null) {
                stack.push(currNode.left);
            }
        }
        System.out.println();
    }

    public void breadthFirstSearch() {
        
        // call wrapper function hidden from API
        if (this.head != null) {
            breadthFirstSearch(this.head);
        }
    }

    private void breadthFirstSearch(Node root) {

        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        Node currNode;
        while (!queue.isEmpty()) { 

            currNode = queue.remove();
            System.out.print(currNode.value + " ");

            if (currNode.left != null) {
                queue.add(currNode.left);
            }

            if (currNode.right != null) {
                queue.add(currNode.right);
            }
        }
        System.out.println();
    }

    public boolean isBalanced() {
        return isBalanced(this.head);
    }

    private boolean isBalanced(Node node) {

        if (node == null) {
            return true;
        }

        int lh;
        int rh;

        lh = getHeight(node.left);
        rh = getHeight(node.right);

        if (Math.abs(lh - rh) <= 1 &&
                isBalanced(node.left) &&
                isBalanced(node.right)) {
            return true;
        }
        return false;
    }


    public int getHeight() {
        return getHeight(this.head);
    }

    private int getHeight(Node node) {
        
        if (node == null) {
            return 0;
        }
        
        return 1 + Math.max(getHeight(node.left), getHeight(node.right));
    }

    /**
     * Helper for BST insertion
     */
    private void add(Node curr, int val) {
        if (curr == null) {
            Node node = new Node(val);
            curr = node;
        }

        if (curr.value > val) {
            add(curr.left, val);
        }
        else {
            add(curr.right, val);
        }
    }

    public Node search(int val) {
        return search(this.head, val);
    }

    private Node search(Node curr, int val) {

        if (curr == null) {
            return null;
        }

        if (curr.value == val) {
            return curr;
        }
        else if (curr.value > val) {
            return search(curr.left, val);
        }
        else {
            return search(curr.right, val);
        }
    }

    private boolean isIdentical(Node root1, Node root2) {
        if (root1 == null && root2 == null) {
            return true;
        }

        if (root1 == null || root2 == null) {
            return false;
        }

        return (root1.value == root2.value &&
                isIdentical(root1.left, root2.left) &&
                isIdentical(root1.right, root2.right));
    }

    public Node getRoot() {
        return this.head;
    }

    public boolean isSubtree(Node tree, Node sub) {
        if (sub == null) {
            return true;
        }

        if (tree == null) {
            return false;
        }

        if (isIdentical(tree, sub)) {
            return true;
        }

        return (isSubtree(tree.left, sub) ||
                isSubtree(tree.right, sub));
    }

    public static void main(String[] args) {
        Node leftRightRightRight = new Node(100);
        Node leftRightRight = new Node(40, null, leftRightRightRight);
        Node rightLeftRight =  new Node(23);
        Node leftLeft = new Node(17);
        Node leftRight = new Node(8, null, leftRightRight);
        Node rightLeft = new Node(11, null, rightLeftRight);
        Node rightRight = new Node(1);
        Node right = new Node(5, rightLeft, rightRight);
        Node left = new Node(7, leftLeft, leftRight);
        Node root = new Node(3, left, right);
        BinaryTree tree = new BinaryTree(root);

        /* resulting output */
        // System.out.print(tree.zigzagTraversal(tree.getRoot()));
        // tree.depthFirstSearch();
//        tree.breadthFirstSearch();
        tree.inOrderTraversal(root);
        System.out.println();
        System.out.println();
        tree.postOrderTraversal(root);
        System.out.println();
        System.out.println();
        tree.preOrderTraversal(root);
        System.out.println();
        System.out.println();
//        System.out.println(tree.findParent(root, 40));

        tree.postOrderNumber(); // O(n) complexity2
        tree.inOrderNumber(); // O(n) complexity
        tree.preOrderNumber(); // O(n) complexity

        System.out.println(tree.head);  // 3
        System.out.println(tree.head.left); // 7
        System.out.println(tree.head.right); // 5
        System.out.println(leftLeft); // 17

        System.out.println();
        System.out.println(tree.isBST());


    }
}   