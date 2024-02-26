import java.util.Scanner;

public class PalindromeChecker {

    public static boolean isPalindrome(int number) {
        String original = Integer.toString(number);
        String reversed = new StringBuilder(original).reverse().toString();
        return original.equals(reversed);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        boolean result = isPalindrome(number);
        System.out.println(result ? "The number is a palindrome." : "The number is not a palindrome.");
        scanner.close();
    }
}
