import numpy as np
import matplotlib.pyplot as plt

# Given points
A = np.array([2, -1])     # Vertex
D = np.array([2.5, -0.5]) # Foot of perpendicular

# Side length of equilateral triangle
a = np.sqrt(2/3)

# Direction vector of the base (perpendicular to normal (1,1))
m = np.array([1, -1]) / np.sqrt(2)   # Unit vector along base

# Base vertices B and C
B = D + (a/2) * m
C = D - (a/2) * m

# Line x+y=2
x = np.linspace(-2, 4, 400)
y = 2 - x

# Plot base line
plt.plot(x, y, 'k-', label=r"$x+y=2$")

# Plot triangle edges
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
plt.plot([A[0], C[0]], [A[1], C[1]], 'b-')
plt.plot([B[0], C[0]], [B[1], C[1]], 'b-')

# Plot altitude AD
plt.plot([A[0], D[0]], [A[1], D[1]], 'r--', label="Altitude")

# Mark points
plt.scatter(*A, color='blue')
plt.text(A[0]+0.1, A[1]-0.2, "A(2,-1)", fontsize=10)

plt.scatter(*D, color='green')
plt.text(D[0]+0.1, D[1], "D(2.5,-0.5)", fontsize=10)

plt.scatter(*B, color='purple')
plt.text(B[0]+0.1, B[1], "B", fontsize=10)

plt.scatter(*C, color='purple')
plt.text(C[0]+0.1, C[1], "C", fontsize=10)

# Axes settings
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Equilateral Triangle with base x+y=2 and vertex A(2,-1)")

plt.show()
