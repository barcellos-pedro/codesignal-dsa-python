def my_sum(nums, total = 0):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return total + nums[0]
    
    total += nums.pop()

    return my_sum(nums,total)

print(my_sum([1,2,3,4,5]))
print(sum([1,2,3,4,5]))