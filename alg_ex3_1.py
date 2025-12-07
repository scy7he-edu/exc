# рекурсия чуть посложнее (далась очень тяжело)
nums = [2, 4, 6]
def sum_recursive(nums):
    num_sum = 0
    first_num = nums[0]
    rest_nums = nums[1:]
    if len(rest_nums) == 0:
        return first_num
    else:
        num_sum = first_num + sum_recursive(rest_nums)
        return num_sum
print(sum_recursive(nums))
