import matplotlib.pyplot as plt
import numpy as np

# Generating sample mining data
np.random.seed(0)
num_samples = 100
mine_depth = np.random.uniform(100, 1000, num_samples)  # Depth of mines
ore_grade = np.random.uniform(0.5, 10, num_samples)     # Ore grade in percentage
production = np.random.uniform(100, 5000, num_samples)  # Annual production in tons

# Creating the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(mine_depth, production, c=ore_grade, cmap='viridis', alpha=0.7)
plt.colorbar(label='Ore Grade (%)')
plt.xlabel('Mine Depth (m)')
plt.ylabel('Annual Production (tons)')
plt.title('Mining Data Visualization')
plt.grid(True)
plt.tight_layout()

# Displaying the plot
plt.show()
