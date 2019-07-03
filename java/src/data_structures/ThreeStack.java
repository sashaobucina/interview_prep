package data_structures;

import java.util.ArrayList;
import java.util.List;

public class ThreeStack {
  public int stackSize;
  private int[] stackPointers = {-1, -1, -1};
  public StackNode[] buffer;
  public List<Integer> freeList = new ArrayList<>();

  public ThreeStack(int stackSize) {
    this.stackSize = stackSize;
    this.buffer = new StackNode[stackSize * 3];

    // Initialize the free list
    for (int i = 0; i < buffer.length; i++) {
      this.freeList.add(i);
    }
  }

  private boolean validStackNum(int stackNum) {
    return stackNum < 3;
  }

  public void push(int stackNum, int data) {
    if (!this.validStackNum(stackNum)) {
      throw new IllegalArgumentException("Stack number must be less than 3!");
    }

    int lastIndex = stackPointers[stackNum];
    stackPointers[stackNum] = this.freeList.get(0);
    freeList.remove(0);
    buffer[stackPointers[stackNum]] = new StackNode(data, lastIndex);
  }

  public int pop(int stackNum) {
    if (!this.validStackNum(stackNum)) {
      throw new IllegalArgumentException("Stack number must be less than 3!");
    }

    int value = buffer[stackPointers[stackNum]].value;
    int lastIndex = stackPointers[stackNum];
    stackPointers[stackNum] = buffer[stackPointers[stackNum]].prev;
    buffer[lastIndex] = null;
    freeList.add(lastIndex);
    return value;
  }

  public int peek(int stackNum) {
    if (!this.validStackNum(stackNum)) {
      throw new IllegalArgumentException("Stack number must be less than 3!");
    }
    return buffer[stackPointers[stackNum]].value;
  }

  public boolean isEmpty(int stackNum) {
    if (!this.validStackNum(stackNum)) {
      throw new IllegalArgumentException("Stack number must be less than 3!");
    }
    return stackPointers[stackNum] == -1;
  }

  public boolean isFull() { return freeList.size() == 0; }

  public void printBuffer() {
    int i = 0;
    while (i < buffer.length - 1) {
      System.out.print(buffer[i] + ", ");
      i++;
    }
    System.out.println(buffer[i]);
  }

  public static void main(String[] args) {
    ThreeStack stack = new ThreeStack(3);
    stack.push(0, 0);
    stack.push(2, 200);
    stack.push(1, 100);
    stack.push(1, 1000);
    stack.pop(0);
    stack.pop(2);
    stack.push(1, 10000);
    stack.push(1, 50);
    stack.push(1, 51);
    stack.push(0, 52);
    stack.push(2, 53);
    stack.push(0, 54);
    stack.push(1, 55);
    stack.printBuffer();
  }

  private class StackNode {
    private int value;
    private int prev;
    StackNode(int val, int prev) {
      this.value = val;
      this.prev = prev;
    }

    @Override
    public String toString() {
      return String.format("{%d, prev: %d}", value, prev);
    }
  }
}