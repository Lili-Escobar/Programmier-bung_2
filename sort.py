
def bubble_sort(power_W):
    n = len(power_W)
    for i in range(n):
        for j in range(0, n-i-1):
            if power_W[j] > power_W[j+1]:
                power_W[j], power_W[j+1] = power_W[j+1], power_W[j] # swap
    return power_W


if __name__ == "__main__":
    # Example usage
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(unsorted_array)
    print("Unsorted array:", unsorted_array)            
    print("Sorted array:", sorted_array)    