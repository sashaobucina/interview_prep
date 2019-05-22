package blockchain;

import java.util.*;
import java.lang.*;
import java.security.MessageDigest;

/**
 * Utility class that provides helper methods in regards to string mainpulation/generation.
 */
public class StringUtil {

    /**
     * Applies SHA256 to a given input string and returns the hashed
     * result.
     * 
     * @param input the String to be hashed
     * @return the resulting hashed string
     */
    public static String applySha256(String input) {
        try {
            MessageDigest msgDigest = MessageDigest.getInstance("SHA-256");
            byte[] hash = msgDigest.digest(input.getBytes("UTF-8"));

            // the hash as a hexadecimal string
            StringBuffer hexString = new StringBuffer();
            for (int i = 0; i < hash.length; i++) {
                String hex = Integer.toHexString(0xff & hash[i]);
                if (hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }
            return hexString.toString();
        } catch (Exception e) {
            System.out.println("ERROR: Failed to apply SHA256 to given string");
            throw new RuntimeException(e);
        }
    }
}
