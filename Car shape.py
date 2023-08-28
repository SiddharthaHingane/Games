import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the body of the car (rectangle)
car_body = patches.Rectangle((0.1, 0.2), 0.6, 0.2, color='blue')
ax.add_patch(car_body)

# Draw the roof of the car (rectangle)
car_roof = patches.Rectangle((0.2, 0.4), 0.4, 0.15, color='blue')
ax.add_patch(car_roof)

# Draw the wheels of the car (circles)
wheel1 = patches.Circle((0.2, 0.1), 0.05, color='black')
wheel2 = patches.Circle((0.6, 0.1), 0.05, color='black')
ax.add_patch(wheel1)
ax.add_patch(wheel2)

# Set aspect ratio and limits
ax.set_aspect('equal')
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.6)

# Remove axes
ax.axis('off')

# Show the plot
plt.show()
