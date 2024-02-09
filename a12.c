
#include <stdio.h>

int fibonacci(int n) {
    int t1 = 0, t2 = 1, nextTerm;

    for (int i = 1; i <= n; ++i) {
        printf("%d, ", t1);
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
    return 0;
}

int isFibonacci(int n) {
    if (n <= 0)
        return 0;
    int t1 = 0, t2 = 1, nextTerm = t1 + t2;
    while (nextTerm < n) {
        t1 = t2;
        t2 = nextTerm;
        nextTerm = t1 + t2;
    }
    return nextTerm == n;
}

int main() {
    int n = 10; // number of terms to be printed
    fibonacci(n);
    int testNumbers[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(testNumbers) / sizeof(testNumbers[0]);
    for (int i = 0; i < size; i++) {
        printf("%d is ", testNumbers[i]);
        if (!isFibonacci(testNumbers[i]))
            printf("not ");
        printf("a Fibonacci number.\n");
    }
    return 0;
}