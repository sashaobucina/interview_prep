package recursion;

import java.util.*;

public class BalancedParantheses {

    public final static Map<Character, Character> paranthesesMap = new HashMap<Character, Character>() {{
        put('}', '{');
        put(']', '[');
        put(')', '(');
    }};

    public static boolean isBalancedIter(String str) {
        Stack<Character> stk = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            Character c = str.charAt(i);
            if (BalancedParantheses.paranthesesMap.values().contains(c)) {
                stk.push(c);
            } else if (BalancedParantheses.paranthesesMap.keySet().contains(c)) {
                if (stk.empty()) { return false; }
                Character peeked = stk.pop();
                if (!BalancedParantheses.paranthesesMap.get(c).equals(peeked)) {
                    return false;
                }
            }
        }
        return stk.empty();
    }

    public static void main(String[] args) {
        System.out.println(BalancedParantheses.isBalancedIter(s));
    }
}
