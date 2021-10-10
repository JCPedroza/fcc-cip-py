"""
This Bubble Sort implementation uses a flag to terminate iterations early if
the list is already sorted.
"""


def bubble_sort(nums: list[float]) -> list[float]:
    for round in range(len(nums) - 1):
        is_sorted = True

        for index in range(len(nums) - round - 1):
            if (nums[index] > nums[index + 1]):
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
                is_sorted = False

        if is_sorted:
            return nums

    return nums
