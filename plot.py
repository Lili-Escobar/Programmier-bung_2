import matplotlib.pyplot as plt
import numpy as np
from load_data import load_data
from sort import bubble_sort    
 

def plot_data(x, y):
    
    plt.figure(figsize=(10, 5))

    # Plot the data
    plt.plot(x, y, label="Leistungskurve", color="red")

    # Add title and labels
    plt.title("Leistung über Zeit")
    plt.xlabel("Zeit [s]")
    plt.ylabel("Leistung [W]")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show() 