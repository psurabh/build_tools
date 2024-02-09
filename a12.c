
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

int main() {
    int n = 10; // number of terms to be printed
    fibonacci(n);
    return 0;
}