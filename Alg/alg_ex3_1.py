# рекурсия
class RecursiveSummer:
    def __init__(self, nums):
        self.nums = nums

    def sum_recursive(self, nums=None):
        if nums is None:
            nums = self.nums

        first_num = nums[0]
        rest_nums = nums[1:]

        if len(rest_nums) == 0:
            return first_num
        else:
            return first_num + self.sum_recursive(rest_nums)

if __name__ == '__main__':
    nums = [2, 4, 6]
    summer = RecursiveSummer(nums)
    print(summer.sum_recursive())
