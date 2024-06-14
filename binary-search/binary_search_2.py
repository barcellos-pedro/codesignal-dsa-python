def binary_search(arr, target):
    low = 0
    high = len(arr)

    while high - low > 1:
        mid = (low + high) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        if mid_value > target:
            high = mid
        else:
            low = mid
    return -1


# Found Cases
print(binary_search([1, 3, 5, 7, 9], 9))
print(binary_search([1, 3, 5, 7, 9], 5))
print(binary_search([1, 3, 9], 9))

# -1 Cases
print(binary_search([1, 3, 5, 7, 9], -1))
print(binary_search([], 3))