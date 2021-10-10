"""
This Bubble Sort implementation will perform all iterations even if the
list is already sorted, but it only iterates through the unsorted
portion of the list.
"""


def bubble_sort(nums: list[float]) -> list[float]:
    for round in range(len(nums) - 1):
        for index in range(len(nums) - round - 1):
            if nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]

    return nums
