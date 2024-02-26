#include <stdio.h>

int add_numbers(int a, int b) {
    return a + b;
}

void test_add_numbers() {
    int result;

    result = add_numbers(1, 2);
    printf("Test 1: %s\n", result == 3 ? "Passed" : "Failed");

    result = add_numbers(-1, -2);
    printf("Test 2: %s\n", result == -3 ? "Passed" : "Failed");

    result = add_numbers(0, 0);
    printf("Test 3: %s\n", result == 0 ? "Passed" : "Failed");

    result = add_numbers(1000, 2000);
    printf("Test 4: %s\n", result == 3000 ? "Passed" : "Failed");

    result = add_numbers(-1000, 2000);
    printf("Test 5: %s\n", result == 1000 ? "Passed" : "Failed");
}

int main() {
    test_add_numbers();
    return 0;
}
