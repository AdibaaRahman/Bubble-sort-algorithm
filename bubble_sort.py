# Bubble Sort Implementation with Optimization in Python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Track if any swap occurred in this pass
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Stop if no swaps happened (list already sorted)

# Sample list to sort
numbers = [4, 5, 1, 3, 2]

# Print the list before and after sorting
print("Before sorting:", numbers)
bubble_sort(numbers)
print("After sorting:", numbers)