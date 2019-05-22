package ctci.chapter02;

import java.util.HashSet;
import java.util.Set;

import ctci.util.LinkedListNode;

public class Question01 {

    public static void removeDuplicates(LinkedListNode node) {
        Set<Integer> set = new HashSet<>();
        LinkedListNode previous = null;

        while (node != null) {
            if (set.contains(node.data) && previous != null) {
                previous.next = node.next;
            } else {
                set.add(node.data);
                previous = node;
            }
            node = node.next;
        }
    }

    public class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
            next = null;
        }
    }

    // Driver
    public static void main(String[] args) {
        LinkedListNode root = new LinkedListNode(1);
        LinkedListNode n1 = new LinkedListNode(2);
        LinkedListNode n2 = new LinkedListNode(3);
        LinkedListNode n3 = new LinkedListNode(3);
        root.next = n1;
        n1.next = n2;
        n2.next = n3;

        System.out.println("Initial: " + root);
        removeDuplicates(root);
        System.out.println("After: " + root);
    }
}
