package ctci.chapter01;

public class Question05 {

    public static String replaceSpaces(String str) {
        if (str == null) throw new IllegalArgumentException("String cannot be null!");

        String replaceString = "02%";
        StringBuilder strBuilder = new StringBuilder();
        for (char c : str.toCharArray()) {
            if (c == ' ') {
                strBuilder.append(replaceString);
            } else {
                strBuilder.append(c);
            }
        }
        return strBuilder.toString();
    }

    // Driver
    public static void main(String[] args) {
        String str = "this is a string";

        String newStr = replaceSpaces(str);
        System.out.println(newStr);
    }
}
