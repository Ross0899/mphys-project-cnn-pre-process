import matplotlib.pyplot as plt
import numpy as np

with open("../cnn/sizes.csv", "r") as f:
    lines = f.readlines()
    radii = [line.strip() for line in lines]

areas = [np.pi * float(r)**2 for r in radii]

plt.hist(areas, bins=20)
plt.xlabel("area (pixels squared")
plt.ylabel("count")
plt.show()