import matplotlib as plt
from plot import plot_data
from load_data import load_data
from sort import bubble_sort
import numpy as np
 

data = load_data('activity.csv')
power_W = data['PowerOriginal']
print(power_W)
sorted_power_W = bubble_sort(power_W)
print(sorted_power_W[::-1])

time = np.arange(len(sorted_power_W))

plot_data(time, sorted_power_W[::-1])

plt.savefig("Leistungskurve.png")