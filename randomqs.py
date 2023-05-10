import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    print("Array:", arr)
    print("Pivot:", pivot)

    lesser = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return randomized_quicksort(lesser) + equal + randomized_quicksort(greater)

# Example usage
array = [9, 4, 6, 2, 5, 1, 8, 3, 7]
print("Before sorting:", array)
sorted_array = randomized_quicksort(array)
print("Sorted array:", sorted_array)