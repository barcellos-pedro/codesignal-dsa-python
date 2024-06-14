def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    
    min = 0
    max = len(arr) - 1

    while min <= max:
        mid = (min + max) // 2
        mid_value = arr[mid]

        if target == mid_value:
            return mid
        if mid_value > target:
            max = mid - 1
        else:
            min = mid + 1
        
    return -1


# Found Cases
print(binary_search([1, 3, 5, 7, 9], 9))
print(binary_search([1, 3, 5, 7, 9], 5))
print(binary_search([1, 3, 9], 9))

# -1 Cases
print(binary_search([1, 3, 5, 7, 9], -1))
print(binary_search([], 3))

# What happens on a reversed sorted array?
print(binary_search([9, 7, 3, 2, 1], 1))