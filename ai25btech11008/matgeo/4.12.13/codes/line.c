#include <stdio.h>
#include <math.h>

int main() {
    // Coordinates of vertex A
    double Ax = 2.0, Ay = -1.0;

    // Foot of perpendicular D
    double Dx = 2.5, Dy = -0.5;

    // Compute distance AD
    double AD = sqrt((Ax - Dx)*(Ax - Dx) + (Ay - Dy)*(Ay - Dy));

    // Side length formula for equilateral triangle
    double a = (2 * AD) / sqrt(3);

    printf("Length of side of the equilateral triangle = %lf\n", a);

    return 0;
}

