import matplotlib.pyplot as plt
from visualizer.animate import draw_array

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            draw_array(arr, highlight_indices=[j, j+1])
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2]
    plt.figure()
    bubble_sort(arr)
    plt.show()
