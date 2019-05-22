package ctci.chapter01;

public class Question08 {

    public static boolean isRotation(String s1, String s2) {
        if (s1.length() != s2.length()) return false;

        String concatenated = s1 + s1;
        return concatenated.contains(s2);
    }

    // Driver
    public static void main(String[] args) {
        String s1 = "waterbottle";
        String s2 = "ttlewaterbo";
        String s3 = "wabottleter";

        System.out.println(isRotation(s1, s2));
        System.out.println(isRotation(s1, s3));
    }
}
