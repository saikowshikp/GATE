import matplotlib.pyplot as plt

# Define the points
points = [(-3, -1), (-2, -1), (-1, 0), (1, 0), (2, 1), (3, 1)]

# Extract x and y coordinates from the points
x_coords, y_coords = zip(*points)

# Plot the line segments without points
plt.plot(x_coords, y_coords, linestyle='-', linewidth=2)

# Set axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Y=h(X)')

# Add bold X and Y axes
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Display the plot
#plt.grid(True)
plt.show()

