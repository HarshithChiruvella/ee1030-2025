import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_geometry(lmbda):
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')

    # Line L1: y=x, z=1
    t = np.linspace(-3, 3, 100)
    x1, y1, z1 = t, t, np.ones_like(t)
    ax.plot(x1, y1, z1, color='blue', label='L1: y=x, z=1')

    # Line L2: y=-x, z=-1
    s = np.linspace(-3, 3, 100)
    x2, y2, z2 = s, -s, -np.ones_like(s)
    ax.plot(x2, y2, z2, color='green', label='L2: y=-x, z=-1')

    # Point P
    P = np.array([lmbda, lmbda, lmbda])
    ax.scatter(*P, color='red', s=60, label=f'P({lmbda},{lmbda},{lmbda})')

    # Foot Q on L1
    Q = np.array([lmbda, lmbda, 1])
    ax.scatter(*Q, color='purple', s=60, label='Q')

    # Foot R on L2
    R = np.array([0, 0, -1])
    ax.scatter(*R, color='orange', s=60, label='R')

    # Draw perpendiculars
    ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], 'r--')
    ax.plot([P[0], R[0]], [P[1], R[1]], [P[2], R[2]], 'r--')

    # Labels and settings
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    ax.set_title(f"Geometry for λ = {lmbda}")
    ax.view_init(elev=20, azim=30)
    plt.show()

# Example: plot for λ = 1
plot_geometry(1)
