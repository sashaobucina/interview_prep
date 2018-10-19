package ctci.chapter01;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Question01 {

    public static final int SET_SIZE = 128;

    public static boolean unique(String str) {
        boolean[] directAccessTable = new boolean[SET_SIZE];

        for (char c : str.toCharArray()) {
            int asciiCode = (int) c;
            if (directAccessTable[asciiCode]) {
                return false;
            }
            directAccessTable[asciiCode] = true;
        }
        return true;
    }

    // Driver
    public static void main(String[] args) throws IOException {
        InputStreamReader in = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(in);
        System.out.println("Enter string to analyze (Type 'N' to exit):");
        while (true) {
            String testStr = br.readLine();
            if (testStr.equals("N")) {
                break;
            }

            if (unique(testStr)) {
                System.out.println("String is unique");
            } else {
                System.out.println("Repeat characters in the string");
            }
        }
        System.out.println("Program terminating ...");
    }
}
