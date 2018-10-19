package ctci.util;

public class LinkedListNode {

    public int data;
    public LinkedListNode next;

    public LinkedListNode(int data) {
        this.data = data;
        this.next = null;
    }

    @Override
    public String toString() {
        StringBuilder strBuilder = new StringBuilder();
        LinkedListNode curr = this;
        while (curr != null) {
            if (curr.next == null) {
                strBuilder.append(String.format("%d -> <end>", curr.data));
            } else {
                strBuilder.append(String.format("%d -> ", curr.data));
            }
            curr = curr.next;
        }
        return strBuilder.toString();
    }

    public static void main(String[] args) {

    }
}
