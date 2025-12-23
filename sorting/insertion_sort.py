import matplotlib.pyplot as plt
from visualizer.animate import draw_array

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            draw_array(arr, highlight_indices=[j, j + 1])
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        draw_array(arr, highlight_indices=[j + 1])

if __name__ == "__main__":
    arr = [9, 5, 1, 4, 3]
    plt.figure()
    insertion_sort(arr)
    plt.show()
