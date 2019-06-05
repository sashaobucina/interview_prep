package leetcode;

import java.util.TreeMap;

public class IntToRoman {
  private final static TreeMap<Integer, String> mapping = new TreeMap<>();

  static {
    mapping.put(1000, "M");
    mapping.put(900, "CM");
    mapping.put(500, "D");
    mapping.put(400, "CD");
    mapping.put(100, "C");
    mapping.put(90, "XC");
    mapping.put(50, "L");
    mapping.put(40, "XL");
    mapping.put(10, "X");
    mapping.put(9, "IX");
    mapping.put(5, "V");
    mapping.put(4, "IV");
    mapping.put(1, "I");
  }

  public static String toRoman(int num) {
    int l = mapping.floorKey(num);
    System.out.println(l);
    if (num == l) {
      return mapping.get(num);
    }
    return mapping.get(l) + toRoman(num - l);
  }

  public static void main(String[] args) {
    System.out.println(IntToRoman.toRoman(901));
  }

}