#include <stdio.h>
#include <math.h>

int main() {
    double lambda_values[] = {1, -1, sqrt(2), -sqrt(2)};
    int n = sizeof(lambda_values) / sizeof(lambda_values[0]);

    printf("Checking valid values of lambda:\n");

    for(int i = 0; i < n; i++) {
        double lambda = lambda_values[i];

        // Point P
        double P[3] = {lambda, lambda, lambda};

        // Point Q (foot on L1)
        double Q[3] = {lambda, lambda, 1};

        // Point R (foot on L2)
        double R[3] = {0, 0, -1};

        // Vectors
        double PQ[3] = {Q[0]-P[0], Q[1]-P[1], Q[2]-P[2]};
        double PR[3] = {R[0]-P[0], R[1]-P[1], R[2]-P[2]};

        // Dot product
        double dot = PQ[0]*PR[0] + PQ[1]*PR[1] + PQ[2]*PR[2];

        // Print result
        if(fabs(dot) < 1e-6) {
            printf("lambda = %.3f is VALID (Right angle satisfied)\n", lambda);
        } else {
            printf("lambda = %.3f is NOT valid (Dot product = %.3f)\n", lambda, dot);
        }
    }

    return 0;
}


