import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define mesh grid
x = np.linspace(0, 6, 30)
y = np.linspace(0, 6, 30)
X, Y = np.meshgrid(x, y)

# Define the three planes
Z1 = 6 - X - Y                      # Plane 1: x + y + z = 6
Z2 = 14 - 2*X - 3*Y                 # Plane 2: 2x + 3y + z = 14
Z3 = (14 - X - 2*Y)/3              # Plane 3: x + 2y + 3z = 14

# Set up plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Animation update function
def update_plot(frame):
    ax.cla()
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_zlim(0, 6)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Gaussian Elimination: Visualizing Planes")

    if frame >= 0:
        ax.plot_surface(X, Y, Z1, alpha=0.5, color='red')
    if frame >= 1:
        ax.plot_surface(X, Y, Z2, alpha=0.5, color='green')
    if frame >= 2:
        ax.plot_surface(X, Y, Z3, alpha=0.5, color='blue')
    if frame == 3:
        ax.scatter(0, 4, 2, color='black', s=50)
        ax.text(0, 4, 2, " (0,4,2)", color='black')

# Animate
ani = animation.FuncAnimation(fig, update_plot, frames=4, interval=2000, repeat_delay=2000)
plt.show()
