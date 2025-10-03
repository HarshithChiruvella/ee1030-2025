#include <stdio.h>

#define N 3  // 3x3 matrix

// Function to calculate determinant of a 3x3 matrix
float determinant(float A[3][3]) {
    float det;
    det = A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
        - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
        + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]);
    return det;
}

// Function to find adjoint of 3x3 matrix
void adjoint(float A[3][3], float adj[3][3]) {
    adj[0][0] =   (A[1][1]*A[2][2] - A[1][2]*A[2][1]);
    adj[0][1] = - (A[0][1]*A[2][2] - A[0][2]*A[2][1]);
    adj[0][2] =   (A[0][1]*A[1][2] - A[0][2]*A[1][1]);

    adj[1][0] = - (A[1][0]*A[2][2] - A[1][2]*A[2][0]);
    adj[1][1] =   (A[0][0]*A[2][2] - A[0][2]*A[2][0]);
    adj[1][2] = - (A[0][0]*A[1][2] - A[0][2]*A[1][0]);

    adj[2][0] =   (A[1][0]*A[2][1] - A[1][1]*A[2][0]);
    adj[2][1] = - (A[0][0]*A[2][1] - A[0][1]*A[2][0]);
    adj[2][2] =   (A[0][0]*A[1][1] - A[0][1]*A[1][0]);

    // Transpose of cofactor matrix = adj(A)
    float temp;
    temp = adj[0][1]; adj[0][1] = adj[1][0]; adj[1][0] = temp;
    temp = adj[0][2]; adj[0][2] = adj[2][0]; adj[2][0] = temp;
    temp = adj[1][2]; adj[1][2] = adj[2][1]; adj[2][1] = temp;
}

// Function to find inverse of 3x3 matrix
int inverse(float A[3][3], float inv[3][3]) {
    float det = determinant(A);
    if (det == 0) {
        printf("Matrix is singular, no inverse exists.\n");
        return 0;
    }

    float adj[3][3];
    adjoint(A, adj);

    for (int i=0; i<3; i++)
        for (int j=0; j<3; j++)
            inv[i][j] = adj[i][j] / det;

    return 1;
}

// Multiply 3x3 matrix with 3x1 vector
void multiply(float A[3][3], float b[3], float x[3]) {
    for (int i=0; i<3; i++) {
        x[i] = 0;
        for (int j=0; j<3; j++)
            x[i] += A[i][j] * b[j];
    }
}

int main() {
    // Define A and b
    float A[3][3] = {
        {1, 2, -3},
        {2, 0, -3},
        {1, 2,  0}
    };
    float b[3] = {1, 2, 3};
    float invA[3][3], x[3];

    // Find inverse
    if (inverse(A, invA)) {
        // Solve x = A^{-1} b
        multiply(invA, b, x);

        printf("Solution:\n");
        printf("x = %.3f\n", x[0]);
        printf("y = %.3f\n", x[1]);
        printf("z = %.3f\n", x[2]);
    }

    return 0;
}



