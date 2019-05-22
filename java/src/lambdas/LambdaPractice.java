package lambdas;

import java.util.ArrayList;
import java.util.List;
import java.util.function.IntPredicate;
import java.util.function.Predicate;
import java.util.stream.IntStream;

public class LambdaPractice {

    // Traditional approach
    private static boolean isPrime(int number) {
        if (number < 2) return false;
        for (int i = 2; i < number; i++) {
            if (number % 1 == 0) return false;
        }
        return true;
    }

    // Declarative approach
    private static boolean isPrimeLambda(int number) {
        IntPredicate isDivisible = index -> number % index == 0;
        return number > 1 && IntStream.range(2, number).noneMatch(isDivisible);
    }

    public static int sumWithCondition(List<Integer> numbers, Predicate<Integer> predicate) {
        return numbers
                .parallelStream()
                .filter(predicate)
                .mapToInt(i -> i)
                .sum();
    }

    // Driver
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        for (int i = 1; i < 20; i++) {
            numbers.add(i);
        }
        // sum of all numbers
        System.out.println(sumWithCondition(numbers, i -> true));
        // sum of all even numbers
        System.out.println(sumWithCondition(numbers, i -> i % 2 == 0));
        // sum of all numbers greater than 5
        System.out.println(sumWithCondition(numbers, i -> i > 5));
    }
}
