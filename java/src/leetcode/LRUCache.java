package leetcode;

import java.lang.*;
import java.util.*;

class Node {

    int key;
    int value;
    Node previous;
    Node next;

    public Node(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

public class LRUCache {

    int capacity;
    Map<Integer, Node> map = new HashMap<>();
    Node head = null;
    Node tail = null;


    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (map.containsKey(key)) {
            Node node = map.get(key);
            remove(node);
            setHead(node);
            return node.value;
        }
        return -1;
    }


    public void set(int key, int value) {
        if (map.containsKey(key)) {
            Node old = map.get(key);
            old.value = value;
            remove(old);
            setHead(old);
        } else {
            Node created = new Node(key, value);
            if (map.size() >= this.capacity) {
                map.remove(this.tail.key);
                remove(this.tail);
                setHead(created);
            } else {
                setHead(created);
            }
            map.put(key, created);
        }
    }

    public void remove(Node node) {
        if (node.previous != null) {
            node.previous.next = node.next;
        } else {
            this.head = node.next;
        }

        if (node.next != null) {
            node.next.previous = node.previous;
        } else {
            this.tail = node;
        }
    }

    public void setHead(Node node) {
        node.next = this.head;
        node.previous = null;

        if (this.head != null) {
            this.head.previous = node;
        }

        this.head = node;

        if (this.tail == null) {
            this.tail = this.head;
        }
    }


    public static void main(String[] args) {
        // Driver
    }

}