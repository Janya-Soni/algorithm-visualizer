import matplotlib.pyplot as plt
from visualizer.animate import draw_array

def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        draw_array(arr, highlight_indices=[k])
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        draw_array(arr, highlight_indices=[k])
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        draw_array(arr, highlight_indices=[k])
        arr[k] = right_part[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    plt.figure()
    merge_sort(arr, 0, len(arr) - 1)
    plt.show()
