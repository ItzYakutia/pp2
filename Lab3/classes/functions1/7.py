def has_33(nums):
    for k in range(1, len(nums)):
        if nums[k-1] == 3 and nums[k] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

