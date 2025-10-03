#include <stdio.h>

int main() {
    // Coefficients of equations
    // Example: 9x + 10y = 42  and  9x + 10y = 14
    float a1 = 9, b1 = 10, c1 = 42;
    float a2 = 9, b2 = 10, c2 = 14;

    // Ratios
    float r1 = a1 / a2;
    float r2 = b1 / b2;
    float r3 = c1 / c2;

    if (r1 == r2 && r2 == r3) {
        printf("Consistent with infinitely many solutions.\n");
    } else if (r1 == r2 && r2 != r3) {
        printf("Inconsistent system (no solution).\n");
    } else {
        printf("Consistent with exactly one solution.\n");
    }

    return 0;
}
