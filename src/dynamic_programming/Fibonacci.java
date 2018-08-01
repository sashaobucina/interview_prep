import java.io.*;
import java.lang.*;
import java.util.*;

public class Fibonacci {

    public Fibonacci() {}

    public static long fib(int n) {
        return (n < 3) ? 1 : fib(n-1) + fib(n-2);
    }

    public static long fibDP() {
        return null;
    }

    public static void main(String[] args) {
        
    }
}