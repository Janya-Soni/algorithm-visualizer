import matplotlib.pyplot as plt
from visualizer.animate import draw_array

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            # Highlight current minimum and current element
            draw_array(arr, highlight_indices=[min_idx, j])

            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_array(arr, highlight_indices=[i])

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    plt.figure()
    selection_sort(arr)
    plt.show()
