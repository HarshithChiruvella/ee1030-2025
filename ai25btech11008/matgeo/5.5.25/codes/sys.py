import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define column vectors of A
a1 = np.array([1,2,1])
a2 = np.array([2,0,2])
a3 = np.array([-3,-3,0])
b  = np.array([1,2,3])

# Scaled components from solution x = [2, 1/2, 2/3]
v1 = 2*a1
v2 = 0.5*a2
v3 = (2/3)*a3

# Step-by-step sum points
origin = np.array([0,0,0])
p1 = v1
p2 = v1+v2
p3 = v1+v2+v3  # should equal b

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Axes limits
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_zlim(-1,4)

# Plot column vectors
ax.quiver(0,0,0, *a1, color='blue', label='a1')
ax.quiver(0,0,0, *a2, color='green', label='a2')
ax.quiver(0,0,0, *a3, color='red', label='a3')
ax.quiver(0,0,0, *b,  color='purple', label='b')

# Plot scaled solution vectors
ax.quiver(0,0,0, *v1, color='blue', alpha=0.5)
ax.quiver(0,0,0, *v2, color='green', alpha=0.5)
ax.quiver(0,0,0, *v3, color='red', alpha=0.5)

# Polygonal chain to show addition step by step
ax.plot([0,p1[0]],[0,p1[1]],[0,p1[2]],'k--')
ax.plot([p1[0],p2[0]],[p1[1],p2[1]],[p1[2],p2[2]],'k--')
ax.plot([p2[0],p3[0]],[p2[1],p3[1]],[p2[2],p3[2]],'k--')

# Labels
ax.text(*a1, "a1", color='blue')
ax.text(*a2, "a2", color='green')
ax.text(*a3, "a3", color='red')
ax.text(*b, "b", color='purple')
ax.text(*v1, "2a1", color='blue')
ax.text(*v2, "1/2 a2", color='green')
ax.text(*v3, "2/3 a3", color='red')

# Axes labels and title
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()
ax.set_title("3D visualization of 2a1 + (1/2)a2 + (2/3)a3 = b")

plt.show()

