import matplotlib as plt

from load_data import load_data
from sort import bubble_sort

data = load_data('activity.csv')
power_W = data['PowerOriginal']
print(power_W)
sorted_power_W = bubble_sort(power_W)
print(sorted_power_W[::-1])