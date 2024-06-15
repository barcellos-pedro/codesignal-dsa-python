import random


def quicksort(arr):
    '''
        Time:
            average O(n log n)
            worst O(n^2) if it's not the most optmized pivot
        Space:
            O(log n)
    '''
    if len(arr) <= 1:
        return arr
    
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]

    left = [num for num in arr if num < pivot]
    right = [num for num in arr if num > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


arr = [3, 1, 99, 5]

print(quicksort([]))
print(quicksort([1]))
print(quicksort([2,1]))
print(quicksort(arr))