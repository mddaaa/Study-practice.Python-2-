nums = [1,1,2,3,4,5]
def numbers_repeat(nums):
    return not sorted(nums) == list(set(nums))

print(numbers_repeat(nums))
