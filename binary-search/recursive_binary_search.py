def binary_search_recursive(arr, target, min = 0, max = None):
    # Edge case
    if len(arr) == 0:
        return -1

    # On first call
    if max == None:
        max = len(arr) - 1

    # Base case to stop recursion
    if min > max:
        return -1
    
    mid = (min + max) // 2 # round floor
    mid_value = arr[mid]

    if target == mid_value:
        return mid
    if mid_value > target:
        max = mid - 1
        return binary_search_recursive(arr, target, min, max)
    else:
        min = mid + 1
        return binary_search_recursive(arr, target, min, max)


# OK
print(binary_search_recursive([1, 3, 5, 7, 9], 9))
print(binary_search_recursive([1, 3, 5, 7, 9], 5))
print(binary_search_recursive([1, 3, 9], 9))

# -1
print(binary_search_recursive([1, 3, 5, 7, 9], 8))
print(binary_search_recursive([], 3))

# What happens on a reversed sorted array?
print(binary_search_recursive([9, 7, 3, 2, 1], 1))
