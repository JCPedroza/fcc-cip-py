from math import inf


def selection_sort(nums: list[float]) -> list[float]:
    for pivot in range(len(nums) - 1):
        min_num, min_num_index = inf, -1

        for target in range(pivot, len(nums)):
            if nums[target] < min_num:
                min_num, min_num_index = nums[target], target

        nums[pivot], nums[min_num_index] = nums[min_num_index], nums[pivot]

    return nums
