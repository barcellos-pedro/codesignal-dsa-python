def merge(left_half, right_half):
    result = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_half) and right_idx < len(right_half):
        left_value = left_half[left_idx]
        right_value = right_half[right_idx]

        if left_value < right_value:
            result.append(left_value)
            left_idx += 1
        else:
            result.append(right_value)
            right_idx += 1

    # get remainder of lists starting
    result += left_half[left_idx:]
    result += right_half[right_idx:]
    return result


def merge_sort(arr):
    '''
        Time:
            best/average/worst O(n log n)
        Space:
            O(n)
    '''
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


print(merge_sort([]))
print(merge_sort([1]))
print(merge_sort([2, 1]))
print(merge_sort([3, 1, 99, 5]))