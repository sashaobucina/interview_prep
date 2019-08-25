package data_structures;

public class DisjointSet {

  private int[] data;

  public DisjointSet(int[] data) {
    this.data = data;
  }

  public int find(int i) {
    if (i != this.data[i]) {
      this.data[i] = this.find(this.data[i]);
    }
    return this.data[i];
  }

  public void union(int i, int j) {
    int pi = this.find(i);
    int pj = this.find(j);
    if (pi != pj) {
      this.data[pi]= this.data[pj];
    }
  }

  public boolean isConnected(int i, int j) {
    return this.find(i) == this.find(j);
  }

  public static void main(String[] args) {
    int[] nums = new int[] {0, 1, 2, 3, 4, 5, 6, 7, 8};
    DisjointSet disjointSet = new DisjointSet(nums);
    disjointSet.union(1, 8);
    System.out.println(disjointSet.find(1));
  }
}