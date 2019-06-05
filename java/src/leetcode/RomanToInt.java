package leetcode;

import java.util.HashMap;
import java.util.Map;

public class RomanToInt {
  private static final Map<Character, Integer> mapping = new HashMap<>();
  
  static {
    mapping.put('I', 1);
    mapping.put('V', 5);
    mapping.put('X', 10);
    mapping.put('L', 50);
    mapping.put('C', 100);
    mapping.put('D', 500);
    mapping.put('M', 1000);
  }

  public static int romanToInt(String numeral) {
    int res = 0;
    int i  = 0;

    while (i < numeral.length()) {
      int s1 = mapping.get(numeral.charAt(i));
      if (i + 1 < numeral.length()) {
        int s2 = mapping.get(numeral.charAt(i+1));
        if (s1 < s2) {
          res += s2 - s1;
          i += 2;
        } else {
          res += s1;
          i++;
        }
      } else {
        res += s1;
        i++;
      }
    }
    return res;
  }

  public static void main(String[] args) {
    System.out.println(RomanToInt.romanToInt("CMI"));
  }
}