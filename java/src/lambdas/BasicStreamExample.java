package lambdas;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class BasicStreamExample {

    // TODO: Add example static methods working with Java Streams and functional programming in Java
    private enum Gender {MALE, FEMALE}

    private static class Person {
         private final String name;
         private final int age;
         private final Gender gender;

         public Person(String name, int age, Gender gender) {
            this.name = name;
            this.age = age;
            this.gender = gender;
         }

         public String getName() {
             return this.name;
         }

         public int getAge() {
             return this.age;
         }

         public Gender getGender() {
             return this.gender;
         }
    }

    private static void printNames(List<Person> persons, Predicate<? super Person> predicate) {
        persons.stream()
                .filter(predicate)
                .map(p -> ((Person) p).getName())
                .forEach(name -> System.out.println(name));
    }


    // Driver
    public static void main(String[] args) {
        List<Person> persons = new ArrayList<>();
        persons.add(new Person("Albert", 80, Gender.MALE));
        persons.add(new Person("Ben", 15, Gender.MALE));
        persons.add(new Person("Charlote", 20, Gender.FEMALE));
        persons.add(new Person("Dean", 6, Gender.MALE));
        persons.add(new Person("Elaine", 17, Gender.FEMALE));

        System.out.println("----------Printing Persons with age less than 18----------");
        printNames(persons, p -> ((Person) p).getAge() < 18);
        System.out.println("\n--------Printing all Males-------------");
        printNames(persons, p -> ((Person) p).getGender() == Gender.MALE);
        System.out.println("\n---------Printing Persons with Names starting With C------------");
        printNames(persons, p -> ((Person)p).getName().startsWith("C"));
    }
}
