import numpy as np
import matplotlib.pyplot as plt

# Define x-range
x = np.linspace(-5, 10, 400)

# Define the two lines: y = (constant - 9x)/10
y1 = (42 - 9*x) / 10   # from 9x + 10y = 42
y2 = (14 - 9*x) / 10   # from 9x + 10y = 14

# Plotting
plt.figure(figsize=(6,6))
plt.plot(x, y1, label=r'$9x+10y=42$', color='blue')
plt.plot(x, y2, label=r'$9x+10y=14$', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.title('Lines: $9x+10y=42$ and $9x+10y=14$ (Parallel, no intersection)')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.3)

plt.show()

